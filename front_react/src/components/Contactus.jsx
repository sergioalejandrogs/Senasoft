import React from 'react'
import {Form, Button, Container, Row} from "react-bootstrap"

export function Contactus() {
    return (
        <>
            <br />
            <br />
            <Container>
                <Row className="justify-content-center">
                    <br />
                    <h2 style={{ textAlign: 'center' }}>Contact Us</h2>
                    <br />
                    <br />
                    <br />
                    <hr />
                    <Form style={{ width: '50rem' }}>
                        <Form.Group className="mb-3" controlId="formBasicName" style={{  }} >
                            <Form.Control type="text" placeholder="First Name" />
                        </Form.Group>
                        <Form.Group className="mb-3" controlId="formBasicLastName">
                            <Form.Control type="text" placeholder="Last Name" />
                        </Form.Group>
                        <Form.Group className="mb-3" controlId="formBasicEmail">
                            <Form.Control type="email" placeholder="example@example.com" />
                        </Form.Group>
                        <Form.Group className="mb-3" controlId="formBasicPhone">
                            <Form.Control type="text" placeholder="Phone number" />
                        </Form.Group>
                        <Form.Group className="mb-3" controlId="formBasicTextArea">
                            <Form.Control as="textarea" rows={7} placeholder="Enter your message for us here. We will contact you back within 48 hours."/>
                        </Form.Group>
                        <div style={{ textAlign: 'center' }}>
                            <Button variant="dark" type="submit">
                                Submit
                            </Button>
                        </div>
                    </Form>
                </Row>
            </Container>
        </>
    )
}
