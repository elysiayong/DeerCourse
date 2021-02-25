import React from 'react';
// import { Link, Redirect, useParams  } from "react-router-dom";
import { Accordion, Button, Card, Col, Form } from "react-bootstrap";

export const SearchBar = () => (
    <Accordion>
        <Form as={Card} bg="light" text="dark">
            <Card.Header>
                <Form.Row>
                    <Form.Group as={Col} xs="auto" style={{ margin: "0" }}>
                        <Form.Control type="text "placeholder="Search for courses..." />
                        <Form.Text></Form.Text>
                    </Form.Group>
                    <Form.Group style={{ margin: "0" }}>
                        <Accordion.Toggle as={Button} eventKey="0">
                            Filter
                        </Accordion.Toggle>
                        <Button type="submit">
                            Search
                        </Button>
                    </Form.Group>
                </Form.Row>
            </Card.Header>
            <Accordion.Collapse eventKey="0">
                <Card.Body>
                    <Card.Title>ADVANCED SEARCH</Card.Title>
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
                            {/* This will be dynamic */}
                            <option>2</option>
                            <option>3</option>
                            <option>4</option>
                            <option>5</option>
                        </Form.Control>
                    </Form.Group>
                </Card.Body>
            </Accordion.Collapse>
        </Form>
    </Accordion>
)