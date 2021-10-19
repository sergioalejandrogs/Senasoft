import React from 'react';
import {Form, Button, Container, Row} from "react-bootstrap";

export function Login() {
    return (
        <>
            <br />
            <br />
            <br />
            <br />
            <br />
            <Container>
                <Row className="justify-content-center">
                    <Form style= {{ width: '30rem' }}>
                        <Form.Group className="mb-3" controlId="formBasicEmail">
                            <Form.Label>Email address: </Form.Label>
                            <Form.Control type="email" placeholder="Enter email" />
                            <Form.Text className="text-muted">
                            We'll never share your email with anyone else.
                            </Form.Text>
                        </Form.Group>

                        <Form.Group className="mb-3" controlId="formBasicPassword">
                            <Form.Label>Password: </Form.Label>
                            <Form.Control type="password" placeholder="Password" />
                        </Form.Group>
                        <Form.Group className="mb-3" controlId="formBasicCheckbox">
                            <Form.Check type="checkbox" label="Remember me" />
                        </Form.Group>
                        <Button variant="dark" type="submit">
                            Submit
                        </Button>
                    </Form>
                </Row>
            </Container>   
        </>
    )
}
