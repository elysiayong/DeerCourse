import React from 'react';
import {Navbar, Nav, NavDropdown} from 'react-bootstrap';
/*import styled from 'styled-components';*/
import logo from '../assets/homeicon.png';

export const NavigationBar = () => (
    <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark" className="main-nav">
        <Navbar.Brand> 
        <a href="/">
        <img src={logo} style={{width:65}} alt="Home"/>
        </a>
        </Navbar.Brand>
    
        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <Navbar.Collapse id="responsive-navbar-nav">

        <Nav className="mr-auto">
            <NavDropdown title="Programs" id="collasible-nav-dropdown">
            <NavDropdown.Item href="/CSC">Computer Science</NavDropdown.Item>
            <NavDropdown.Divider />
            <NavDropdown.Item href="#action/3.1">...</NavDropdown.Item>
            </NavDropdown>
        </Nav>

        <Nav>
            <Nav.Link href="/login">Login</Nav.Link>
        </Nav>
        </Navbar.Collapse>
    </Navbar>
)