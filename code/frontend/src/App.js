import './App.css';
import {Navbar, Nav, NavDropdown, Jumbotron, Button} from 'react-bootstrap'
import logo from './homeicon.png';
import bgimage from './bg-image.jpg';

function App() {
  return (
    <div className="App">

      <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark" className="main-nav">
        <Navbar.Brand> 
          <a href="#">
          <img src={logo} style={{width:65}} />
          </a>
        </Navbar.Brand>
        
        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <Navbar.Collapse id="responsive-navbar-nav">

          <Nav className="mr-auto">
            <NavDropdown title="Programs" id="collasible-nav-dropdown">
              <NavDropdown.Item href="#action/3.1">Computer Science</NavDropdown.Item>
              <NavDropdown.Item href="#action/3.2">Mathematics</NavDropdown.Item>
              <NavDropdown.Divider />
              <NavDropdown.Item href="#action/3.3">...</NavDropdown.Item>
            </NavDropdown>
          </Nav>

          <Nav>
            <Nav.Link href="#login">Login</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Navbar>

      <br></br>

      <h1>TITLE/LOGO</h1>    
    
    </div>
  );
}

export default App;
