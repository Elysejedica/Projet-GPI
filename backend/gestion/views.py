from .models import Livre, Emprunt
from .models import Reservation
from .models import Notification
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Livre


def liste_livres(request):
    livres = Livre.objects.all()
    return render(request, 'gestion/liste_livres.html', {'livres': livres})


@login_required
def emprunter_livre(request, livre_id):
    livre = get_object_or_404(Livre, id=livre_id)

    if livre.stock_disponible < 1:
        return render(request, 'gestion/message.html', {'message': 'Ce livre n\'est pas disponible pour le moment.'})

    date_retour = timezone.now().date() + timedelta(days=14)

    Emprunt.objects.create(
        utilisateur=request.user,
        livre=livre,
        date_retour_prevue=date_retour,
        statut='en cours'
    )
    livre.stock_disponible -= 1
    livre.save()

    return render(request, 'gestion/message.html', {'message': f'Livre emprunté avec succès. Retour prévu le {date_retour}.'})



def reserver_livre(request, livre_id):
    livre = get_object_or_404(Livre, id=livre_id)

    deja_reserve = Reservation.objects.filter(utilisateur=request.user, livre=livre, statut='en attente').exists()
    if deja_reserve:
        return render(request, 'gestion/message.html', {'message': 'Vous avez déjà réservé ce livre.'})

    Reservation.objects.create(
        utilisateur=request.user,
        livre=livre
    )
    return render(request, 'gestion/message.html', {'message': 'Livre réservé avec succès !'})

    def mes_notifications(request):
    notifications = Notification.objects.filter(utilisateur=request.user).order_by('-date_envoi')
    return render(request, 'gestion/notifications.html', {'notifications': notifications})

    
    def retourner_livre(request, emprunt_id):
    emprunt = get_object_or_404(Emprunt, id=emprunt_id, utilisateur=request.user)

    if emprunt.statut == 'retourne':
        return render(request, 'gestion/message.html', {'message': 'Ce livre a déjà été retourné.'})

    emprunt.statut = 'retourne'
    emprunt.save()

    emprunt.livre.stock_disponible += 1
    emprunt.livre.save()

    notifier(request.user, f'Vous avez retourné le livre "{emprunt.livre.titre}". Merci !')

    return render(request, 'gestion/message.html', {'message': 'Livre retourné avec succès !'})


    @login_required
def mes_emprunts(request):
    emprunts = Emprunt.objects.filter(utilisateur=request.user).order_by('-date_emprunt')
    return render(request, 'gestion/mes_emprunts.html', {'emprunts': emprunts})







def get_books(request):
    books = [{"titre": "Django pour les nuls"}, {"titre": "React Master"}]
    return Response(books)