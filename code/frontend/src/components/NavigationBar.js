import React from 'react';
import {Navbar, Nav, NavDropdown} from 'react-bootstrap';
/*import styled from 'styled-components';*/
import logo from '../assets/deer.png';

export const NavigationBar = () => (
    <Navbar collapseOnSelect style={{width: "100%"}} expand="lg" bg="dark"xs variant="dark" className="main-nav">
        <Navbar.Brand> 
        <a href="/">
            <img src={logo} style={{width:50}} alt="Home"/>
        </a>
        </Navbar.Brand>
    
        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <Navbar.Collapse id="responsive-navbar-nav">

        <Nav className="mr-auto">
            <NavDropdown className="navbar-programs" title="Programs" id="collasible-nav-dropdown">
                <NavDropdown.Item className="navbar-csc" href="/CSC">Computer Science</NavDropdown.Item>
                <NavDropdown.Divider />
                <NavDropdown.Item href="#action/3.1">...</NavDropdown.Item>
                <NavDropdown.Divider />
                <NavDropdown.Item href="/Programs">All Programs</NavDropdown.Item>
            </NavDropdown>
        </Nav>

        <Nav>
            <Nav.Link className="navbar-login" href="/login">Login</Nav.Link>
        </Nav>
        </Navbar.Collapse>
    </Navbar>
)

