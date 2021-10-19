import React from 'react'
import { Route, Switch, BrowserRouter as Router } from "react-router-dom";
import {Nav, Navbar, Form, FormControl, Button} from "react-bootstrap";
import 'bootstrap/dist/css/bootstrap.min.css';
import { Home } from "./Home";
import { Login } from "./Login";
import { About } from "./About";
import { Users } from "./Users";
import { Contactus } from "./Contactus";

const Principal = () => {
    return (
        <div className="carcontainer">
            <Router>
                <Navbar bg="dark" variant="dark" style={{ height: '70px' }}>
                    <Navbar.Brand href="/" style={{ margin: '15px' }}>Home</Navbar.Brand>
                    <Nav className="navbar-nav mx-auto">
                        <Nav.Link href="/login" style={{ margin: '15px' }}>Login</Nav.Link>
                        <Nav.Link href="/about" style={{ margin: '15px' }}>About Us</Nav.Link>
                        <Nav.Link href="/users" style={{ margin: '15px' }}>Users</Nav.Link>
                        <Nav.Link href="/contactus" style={{ margin: '15px' }}>Contact Us</Nav.Link>
                    </Nav>
                    <Form className="d-flex" style={{ margin: '15px' }}>
                        <FormControl type="text" placeholder="Search" className="mr-sm-2" style={{ margin: '15px' }} />
                        <Button variant="outline-info" style={{ margin: '15px' }} >Search</Button>
                    </Form>
                </Navbar>    
                <Switch>
                    <Route path="/" exact component={ Home }></Route>
                    <Route path="/login" exact component={ Login }></Route>
                    <Route path="/about" exact component={ About }></Route>
                    <Route path="/users" exact component={ Users }></Route>
                    <Route path="/contactus" exact component={ Contactus }></Route>
                </Switch>
            </Router>
        </div>
    )
}

export default Principal
