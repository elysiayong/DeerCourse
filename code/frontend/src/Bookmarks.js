import React from 'react'
import { Container, Accordion, Card, Button } from 'react-bootstrap'
import { Content } from './components/StyledComponents'

export const Bookmarks = () => {

    return (
        <Content>
            <h1>My Bookmarks</h1>
            {/* Refactor this part of the code. 
                Compartamentalize the container into a different file once
                final design decision has been made.
            */}
            <Container>
                <Accordion defaultActiveKey="0">
                    <Card>
                        <Card.Header>
                        <Accordion.Toggle as={Button} variant="link" eventKey="0">
                            Click me!
                        </Accordion.Toggle>
                        </Card.Header>
                        <Accordion.Collapse eventKey="0">
                        <Card.Body>Hello! I'm the body</Card.Body>
                        </Accordion.Collapse>
                    </Card>
                    <Card>
                        <Card.Header>
                        <Accordion.Toggle as={Button} variant="link" eventKey="1">
                            Click me!
                        </Accordion.Toggle>
                        </Card.Header>
                        <Accordion.Collapse eventKey="1">
                        <Card.Body>Hello! I'm another body</Card.Body>
                        </Accordion.Collapse>
                    </Card>
                    </Accordion>
            </Container>
        </Content>
    )
}