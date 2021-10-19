import React from 'react'
import {Carousel} from 'react-bootstrap'
import "./Card.css"

export function About() {
    return (
        <>
            <Carousel className="carousel">
                <Carousel.Item>
                    <img
                    className="images"
                    src="https://pbs.twimg.com/media/E49anRqWQAAPJvE.jpg"
                    alt="First slide" 
                    />
                    <Carousel.Caption>
                    <h3>First slide label</h3>
                    <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
                    </Carousel.Caption>
                </Carousel.Item>
                <Carousel.Item>
                    <img
                    className="images"
                    src="https://i.imgur.com/R3D8lll.jpg"
                    alt="Second slide"
                    />

                    <Carousel.Caption>
                    <h3>Second slide label</h3>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                    </Carousel.Caption>
                </Carousel.Item>
                <Carousel.Item>
                    <img
                    className="images"
                    src="https://64.media.tumblr.com/cfc752eca45c5027f301264ee6eb4bfb/tumblr_inline_pivxvlStGR1upiwjr_1280.png"
                    alt="Third slide" 
                    />

                    <Carousel.Caption>
                    <h3>Third slide label</h3>
                    <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur.</p>
                    </Carousel.Caption>
                </Carousel.Item>
                </Carousel>
                <br />
                <br />
                <h1 style={{ textAlign: 'center' }}>ABOUT US</h1>
                <br />
                <p style={{ textAlign: 'center' }}>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Fuga ratione omnis saepe molestias sint quisquam alias nesciunt hic sapiente, amet dolorem praesentium in, optio esse, repellat perspiciatis quod nam eius! Lorem ipsum dolor sit amet consectetur adipisicing elit. Officia delectus minima numquam corrupti tempora fugit aliquam similique, repudiandae laboriosam quae nemo eos nisi nesciunt error. Error ex quis voluptas. Commodi? </p>
                <br />
                <p style={{ textAlign: 'center' }}>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Fuga ratione omnis saepe molestias sint quisquam alias nesciunt hic sapiente, amet dolorem praesentium in, optio esse, repellat perspiciatis quod nam eius! Lorem ipsum dolor sit amet consectetur adipisicing elit. Officia delectus minima numquam corrupti tempora fugit aliquam similique, repudiandae laboriosam quae nemo eos nisi nesciunt error. Error ex quis voluptas. Commodi? </p>
        </>
    )
}
