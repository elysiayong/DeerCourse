import React, { useState } from "react";
import { Accordion, Button, Card, Col, Form } from "react-bootstrap";
import magnifyglass from "../assets/searchglass.png";

export const SearchBar = (props) => {
  const [course, setCourse] = useState("");
  const [level, setLevel] = useState("");
  const [duration, setDuration] = useState("");

  const handleSubmit = (e) => {
    console.log(course);
    console.log(level);
    console.log(duration);
    e.preventDefault();
  };

  let searchbar;
  if (props.hasOwnProperty("showFilter") && props.showFilter) {
    // Form has advanced search options
    if (props.hasOwnProperty("collapsible") && props.collapsible) {
      // Form is collapsible
      searchbar = (
        <CollapsibleSearchBar
          course={course}
          setCourse={setCourse}
          level={level}
          setLevel={setLevel}
          duration={duration}
          setDuration={setDuration}
        />
      );
    } else {
      // Form is not collapsible
      searchbar = (
        <NonCollapsibleSearchBar
          course={course}
          setCourse={setCourse}
          level={level}
          setLevel={setLevel}
          duration={duration}
          setDuration={setDuration}
        />
      );
    }
  } else {
    searchbar = <SimpleSearchBar course={course} setCourse={setCourse} />;
  }

  return <Form onSubmit={handleSubmit}>{searchbar}</Form>;
};

const SimpleSearchBar = ({ course, setCourse }) => {
  return (
    <Form.Row xs={2}>
      <Col xs="auto">
        <Form.Control
          type="text"
          placeholder="Search for courses..."
          value={course}
          onChange={(e) => setCourse(e.target.value)}
        />
      </Col>
      <Col>
        <Button type="submit">
          <img src={magnifyglass} style={{ width: 25 }} alt="Search" />
        </Button>
      </Col>
    </Form.Row>
  );
};

const AdvancedSearchOption = ({ level, setLevel, duration, setDuration }) => {
  return (
    <React.Fragment>
      <Form.Group as={Form.Row} controlId="year">
        <Form.Label column>Level</Form.Label>
        <Col>
          {["000", "100", "200", "300", "400"].map((lvl) => (
            <Form.Check
              key={lvl}
              type="radio"
              label={lvl}
              name={lvl}
              checked={lvl === level}
              onChange={() => setLevel(lvl)}
            />
          ))}
        </Col>
      </Form.Group>

      <Form.Group as={Form.Row} controlId="duration">
        <Form.Label column>Duration</Form.Label>
        <Col>
          {["H", "Y"].map((dur) => (
            <Form.Check
              key={dur}
              type="radio"
              label={dur}
              name={dur}
              checked={dur === duration}
              onChange={() => setDuration(dur)}
            />
          ))}
        </Col>
      </Form.Group>
    </React.Fragment>
  );
};

const NonCollapsibleSearchBar = ({
  course,
  setCourse,
  level,
  setLevel,
  duration,
  setDuration,
}) => (
  <React.Fragment>
    <SimpleSearchBar course={course} setCourse={setCourse} />
    <br />
    <h5>ADVANCED SEARCH</h5>
    <AdvancedSearchOption
      level={level}
      setLevel={setLevel}
      duration={duration}
      setDuration={setDuration}
    />
  </React.Fragment>
);

const CollapsibleSearchBar = ({
  course,
  setCourse,
  level,
  setLevel,
  duration,
  setDuration,
}) => (
  <Accordion>
    <Card.Header>
      <SimpleSearchBar course={course} setCourse={setCourse} />
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
        <AdvancedSearchOption
          level={level}
          setLevel={setLevel}
          duration={duration}
          setDuration={setDuration}
        />
      </Card.Body>
    </Accordion.Collapse>
  </Accordion>
);
