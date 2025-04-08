import "./inscription.css"
function Livres() {

return (
    <>
    
    <h1>Inscription</h1>
    <div id="up">
    <input type="text" placeholder="Nom"/>
    <input type="text" placeholder="Prenom"/>
    <input type="email" name="" id="mail" placeholder="Email"/>
    <input type="text" name="" id="num" placeholder="Numéro d étudiant"/>
    <input type="password" name="" id="mdp" placeholder="Mot de pass" />
    </div>
    <div>
        <h2>Rôle</h2>
        <select name="" id="">
            <option value="">Etudiant</option>
            <option value="">Ensignant</option>
        </select>
    </div>
    <div id="SA">
    <a href="#"><button id="but1">S'INSCRIRE</button></a>
    <a href="/Login" id="but2">ANNULER</a>
    </div>
    </>
)
}

export default Livres
