import React from 'react'
import Tarjetas from './Tarjetas'
import { Row } from 'react-bootstrap'

export function Users() {
    return (
        <Row className="justify-content-center">
            <hr />
            <h1 style={{ textAlign: 'center' }}>These are some of our users</h1>
            <Tarjetas />
        </Row>
    )
}
