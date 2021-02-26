import React from "react";
import { Accordion, Button, Card, Col, Form } from "react-bootstrap";
import magnifyglass from "../assets/searchglass.png";

export const SearchBar = (props) => {
  const handleSubmit = (e) => {
    console.log("idk how to redirect form data to another page yet");
    e.preventDefault();
  };

  let searchbar;
  if (props.hasOwnProperty("showFilter") && props.showFilter) {
    // Form has advanced search options
    if (props.hasOwnProperty("collapsible") && props.collapsible) {
      // Form is collapsible
      searchbar = <CollapsibleSearchBar />;
    } else {
      // Form is not collapsible
      searchbar = <NonCollapsibleSearchBar />;
    }
  } else {
    searchbar = <SimpleSearchBar />;
  }

  return <Form onSubmit={handleSubmit}>{searchbar}</Form>;
};

const SimpleSearchBar = () => (
  <Form.Row xs={2}>
    <Col xs="auto">
      <Form.Control type="text" placeholder="Search for courses..." />
    </Col>
    <Col>
      <Button type="submit">
        <img src={magnifyglass} style={{ width: 25 }} alt="Search" />
      </Button>
    </Col>
  </Form.Row>
);

const AdvancedSearchOption = () => (
  <React.Fragment>
    <Form.Group controlId="year">
      <Form.Control as="select" size="sm" custom>
        <option hidden>Year</option>
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
        <option value="4">4</option>
      </Form.Control>
    </Form.Group>
    <Form.Group controlId="session">
      <Form.Control as="select" size="sm" custom>
        <option hidden>Session</option>
        <option value="f">Fall</option>
        <option value="w">Winter</option>
        <option value="s">Summer</option>
      </Form.Control>
    </Form.Group>
    <Form.Group controlId="subject">
      <Form.Control as="select" size="sm" custom>
        <option hidden>Subject Area</option>
        <option>Will be updated to be dynamic</option>
        <option>1</option>
        <option>2</option>
        <option>3</option>
        <option>4</option>
      </Form.Control>
    </Form.Group>
  </React.Fragment>
);

const NonCollapsibleSearchBar = () => (
  <React.Fragment>
    <SimpleSearchBar />
    <br />
    <h5>ADVANCED SEARCH</h5>
    <AdvancedSearchOption />
  </React.Fragment>
);

const CollapsibleSearchBar = () => (
  <Accordion>
    <Card.Header>
      <SimpleSearchBar />
      <Form.Row>
        <Col xs>
          <Accordion.Toggle as={Button} eventKey="0">
            Filter
          </Accordion.Toggle>
        </Col>
      </Form.Row>
    </Card.Header>
    <Accordion.Collapse eventKey="0">
      <Card.Body>
        <Card.Title>ADVANCED SEARCH</Card.Title>
        <AdvancedSearchOption />
      </Card.Body>
    </Accordion.Collapse>
  </Accordion>
);
