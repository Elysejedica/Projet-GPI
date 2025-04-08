import "./Login.css"
function Login() {

return (
    <>
    
    <h1>LOG IN</h1>
    <div id="up">
    <input type="text" placeholder="Nom"/>
    <input type="text" placeholder="Prenom"/>
    <input type="email" name="" id="mail" placeholder="Email"/>
    <input type="text" name="" id="num" placeholder="Numéro d étudiant"/>
    
    <select name="">
            <option value="">Etudiant</option>
            <option value="">Ensignant</option>
    </select>
    
    
    <input type="password" name="" id="mdp" placeholder="Mot de pass" />
    </div>
   
    <div id="SA">
    <a href="/livres" id="buta">S'INSCRIRE</a>
    <a href="/Bibliotheque"><button id="butb">SE CONNECTER</button></a>
    </div>
    </>
)
}

export default Login
