import React from "react";
import { Accordion, Button, Card, Col, Form } from "react-bootstrap";
import { Redirect } from "react-router";
import magnifyglass from "../assets/searchglass.png";

const lvls = ["000", "100", "200", "300", "400"];
const durs = ["H", "Y"];

export const SearchBar = ({// unpacking all states from parent element
  showFilter,
  collapsible,
  code,
  setCode,
  level,
  setLevel,
  duration,
  setDuration,
  redirect,
  setRedirect,
}) => {
  const handleSubmit = (e) => {
    console.log(code);

    // Validate user input
    var isValid = true;

    // Whitelist level
    if (level !== "" && !lvls.includes(level)) {
      console.log("Invalid level");
      setLevel("");
      isValid = false;
    }
    // Whitelist duration
    if (duration !== "" && !durs.includes) {
      console.log("Invalid duration");
      setDuration("");
      isValid = false;
    }

    // Actions after determining user input is valid
    if (isValid) {
      console.log("Form input is valid");
      setRedirect(true);
    } else {
      console.log("Form input is invalid");
    }
    e.preventDefault();
  };

  if (redirect) {
    console.log("Redirecting!");
    // Issue on first search. Will try to set state for component Home while rendering
    // the search bar.
    setRedirect(false); 
    return (
      <Redirect
        to={{ pathname: "/search", state: { code, level, duration } }}
      />
    );
  }

  let searchbar;
  if (showFilter) {
    // Form has advanced search options
    if (collapsible) {
      // Form is collapsible
      searchbar = (
        <CollapsibleSearchBar
          code={code}
          setCode={setCode}
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
          code={code}
          setCode={setCode}
          level={level}
          setLevel={setLevel}
          duration={duration}
          setDuration={setDuration}
        />
      );
    }
  } else {
    searchbar = <SimpleSearchBar code={code} setCode={setCode} />;
  }

  return <Form onSubmit={handleSubmit}>{searchbar}</Form>;
};

const SimpleSearchBar = ({ code, setCode }) => {
  return (
    <Form.Row xs={2}>
      <Col xs="auto">
        <Form.Control
          type="text"
          placeholder="Search for courses..."
          value={code}
          onChange={(e) => setCode(e.target.value)}
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
  const handleLevelSelect = (lvl) => {
    if (lvl !== level) setLevel(lvl);
    else setLevel("");
  };
  const handleDurSelect = (dur) => {
    if (dur !== duration) setDuration(dur);
    else setDuration("");
  };
  return (
    <React.Fragment>
      <Form.Group as={Form.Row} controlId="year">
        <Form.Label column>Level</Form.Label>
        <Col>
          {lvls.map((lvl) => (
            <Form.Check
              key={lvl}
              label={lvl}
              name={lvl}
              onChange={() => handleLevelSelect(lvl)}
              checked={lvl === level}
            />
          ))}
        </Col>
      </Form.Group>

      <Form.Group as={Form.Row} controlId="duration">
        <Form.Label column>Duration</Form.Label>
        <Col>
          {durs.map((dur) => (
            <Form.Check
              key={dur}
              label={dur}
              name={dur}
              onChange={() => handleDurSelect(dur)}
              checked={dur === duration}
            />
          ))}
        </Col>
      </Form.Group>
    </React.Fragment>
  );
};

const NonCollapsibleSearchBar = ({
  code,
  setCode,
  level,
  setLevel,
  duration,
  setDuration,
}) => (
  <React.Fragment>
    <SimpleSearchBar code={code} setCode={setCode} />
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
  code,
  setCode,
  level,
  setLevel,
  duration,
  setDuration,
}) => (
  <Accordion>
    <Card.Header>
      <SimpleSearchBar code={code} setCode={setCode} />
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
