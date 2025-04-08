import React, { useEffect, useState } from 'react';

function BookList() {
const [books, setBooks] = useState([]);

useEffect(() => {
    fetch('http://localhost:8000/api/books/')
    .then(res => res.json())
    .then(data => setBooks(data));
}, []);

return (
    <div>
    <h2>Livres disponibles</h2>
    <ul>
        {books.map((book, index) => (
        <li key={index}>{book.titre}</li>
        ))}
    </ul>
    </div>
);
}

export default BookList;
