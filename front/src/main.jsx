import './index.css'
import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router";
import App from "./app";
import Livres from './pages/Livres';
import Login from './pages/Login';
import Auths from './pages/Auths';
import Recherche from './pages/Recherche';
import Retour from './pages/Retour';
import Formulaire from './pages/Formulaire';
import Bibliotheque from './pages/Bibliotheque';

const root = document.getElementById("root");

ReactDOM.createRoot(root).render(
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<App />} />
      <Route path="/livres" element={<Livres />} />
      <Route path="/Login" element={<Login />} />
      <Route path="/auths" element={<Auths />} />
      <Route path="/recherche" element={<Recherche />} />
      <Route path="/Retour" element={<Retour />} />
      <Route path="/Formulaire" element={<Formulaire />} />
      <Route path="/Bibliotheque" element={<Bibliotheque />} />
    </Routes>
  </BrowserRouter>
);