import "./Formulaire.css"
function Formulaire() {

return (
    <>
    <h1>Formulaire d'emprunt</h1>
    <div id="retour">
    <input type="text" placeholder="Nom de l'emprunteur" />
    <input type="text" placeholder="Titre du livre"/>
    <input type="text" placeholder="Date d'emprunt "/>
    <button>VALIDER</button>
    </div>
    </>
)
}

export default Formulaire
