import React from 'react';
import Card from "./Card";

const Tarjetas = () => {
    const datos = [
        {
          "lang": "Ana",
          "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTg1tUxT2qnPn_WQhWQAwYXW99JaTA_aokLqtBctb2Fct_0BcSPJh6akMKy6uNdRyDTD0M&usqp=CAU",
          "fcolor": "#aaa",
          "scolor": "#fff"
        },
        {
          "lang": "Enrique",
          "url": "https://toppng.com/uploads/preview/ensando-especialmente-en-las-personas-con-movilidad-imagenes-de-personas-115628913400renbsc9lk.png",
          "fcolor": "#aaa",
          "scolor": "#fff"
        },
        {
          "lang": "Lorena",
          "url": "https://c0.klipartz.com/pngpicture/780/973/gratis-png-odontologia-laxmi-marketing-y-ventas-mujer-mujer.png",
          "fcolor": "#aaa",
          "scolor": "#fff"
        },
        {
          "lang": "Sebastian",
          "url": "https://c0.klipartz.com/pngpicture/489/835/gratis-png-pulgar-senal-hombre-persona-hombre.png",
          "fcolor": "#aaa",
          "scolor": "#fff"
        },
        {
          "lang": "Mariana",
          "url": "https://c0.klipartz.com/pngpicture/780/973/gratis-png-odontologia-laxmi-marketing-y-ventas-mujer-mujer.png",
          "fcolor": "#aaa",
          "scolor": "#fff"
        }
    ];

    return (
        <>
            {
                datos.map( 
                    (obj) => {
                        return <Card 
                        key = {obj.lang} 
                        lang = {obj.lang} 
                        url = {obj.url} 
                        fcolor = {obj.fcolor} 
                        scolor = {obj.scolor} 
                        />
                    }
                )
            }
        </>
    )
}

export default Tarjetas
