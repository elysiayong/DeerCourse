import React from 'react';
// import { Link, Redirect, useParams  } from "react-router-dom";
import { Accordion, Button, Card, Form } from "react-bootstrap";

export const SearchBar = () => (
    <Accordion>
        <Card>
            <Card.Header>
                <Form inline>
                    <Form.Control placeholder="Search for courses..." />
                    <Form.Text></Form.Text>
                    <Accordion.Toggle as={Button} eventKey="0">
                        Filter
                    </Accordion.Toggle>
                    <Button type="submit">
                        Search
                    </Button>
                </Form>
            </Card.Header>
            <Accordion.Collapse eventKey="0">
                <Card.Body>
                    ADVANCED SEARCH
                    <Form inline>
                        <Form.Group controlId="year">
                            <Form.Control as="select" size="sm" custom>
                                <option>Year</option>
                                <option>2</option>
                                <option>3</option>
                                <option>4</option>
                                <option>5</option>
                            </Form.Control>
                        </Form.Group>
                        <Form.Group controlId="session">
                            <Form.Control as="select" size="sm" custom>
                                <option>Session</option>
                                <option>2</option>
                                <option>3</option>
                                <option>4</option>
                                <option>5</option>
                            </Form.Control>
                        </Form.Group>
                        <Form.Group controlId="subject">
                            <Form.Control as="select" size="sm" custom>
                                <option>Subject Area</option>
                                <option>2</option>
                                <option>3</option>
                                <option>4</option>
                                <option>5</option>
                            </Form.Control>
                        </Form.Group>
                    </Form>
                </Card.Body>
            </Accordion.Collapse>
        </Card>
    </Accordion>
)