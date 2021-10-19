import React from 'react';
import "./Card.css";

const Card = ( {lang , url , fcolor , scolor} ) => {
    return (
        <div className="card"
            style={{ 
                background : `linear-gradient(to left, ${fcolor}, ${scolor})`
             }}
        >
            <img src={url} alt="Imagen de prueba" class="img"/>
            <h3>{lang}</h3>
        </div>
    )
}

export default Card
