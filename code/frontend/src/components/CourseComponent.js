import React, { useState } from "react";
import {
  Col,
  Container,
  Row,
  ToggleButton,
  ToggleButtonGroup,
} from "react-bootstrap";
import { Link } from "react-router-dom";

export const CourseComponent = ({ courseName, courseInfo }) => {
  const [bookmark, setBookmark] = useState("Bookmark");

  // Course link formatter
  const CourseLinks = ({ type }) => {
    if (
      courseInfo.hasOwnProperty(type) &&
      Array.isArray(courseInfo[type]) &&
      courseInfo[type].length
    )
      return (
        <p>
          {courseInfo[type].map((item) => {
            var link = (
              <Link key={item} to={"/course/" + item}>
                {item}
              </Link>
            );
            return <React.Fragment>{link} </React.Fragment>;
          })}
        </p>
      );
    else return <p>N/A</p>;
  };

  return (
    <React.Fragment>
      <Container>
        <Row>
          <Col>
            <h1>
              {courseName}
              <ToggleButtonGroup
                style={{ margin: 5 }}
                type="checkbox"
                onChange={(e) =>
                  setBookmark(
                    // Temporary bookmarking function
                    bookmark === "Bookmark" ? "Bookmark ✓" : "Bookmark"
                  )
                }
              >
                <ToggleButton
                  className="bookmarkButton"
                  type="checkbox"
                  style={{ padding: "5px" }}
                >
                  {bookmark}
                </ToggleButton>
              </ToggleButtonGroup>
            </h1>
          </Col>
        </Row>
        <br />
        <p>{courseInfo["description"]}</p>
        <Row>
          <Col md>
            <h5>Prerequisites</h5>
            <CourseLinks type={"prerequisites"} />
          </Col>
          <Col md>
            <h5>Corequisites</h5>
            <CourseLinks type={"corequisites"} />
          </Col>
        </Row>
        <Row>
          <Col md>
            <h5>Exclusions</h5>
            <CourseLinks type={"exclusions"} />
          </Col>
          {/* <Col md>
            <h5>Dependent Courses</h5>
            <CourseLinks type={"prerequisite_for"} />
          </Col> */}
        </Row>
      </Container>
    </React.Fragment>
  );
};
