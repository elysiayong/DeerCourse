import React from "react";
import { Container, Row, Col } from "react-bootstrap";
import { Link } from "react-router-dom";
import DATA from "./program_data.json"; // Temporary course info "database"

export const CourseInfo = (courseName) => {
  const courseInfo = tryFetchCourse(courseName);

  // Temporary course link formatter
  const CourseLinks = ({ type }) => {
    if (courseInfo.hasOwnProperty(type) && Array.isArray(courseInfo[type]) && courseInfo[type].length)
      return (
        <p>
          {courseInfo[type].map((item, index) => {
            var link = <Link to={"/course/" + item}>{item}</Link>;
            return <React.Fragment>{link} </React.Fragment>;
          })}
        </p>
      );
    else return <p>N/A</p>;
  };

  if (courseInfo) {
    return (
      <React.Fragment>
        <Container>
          <h1>{courseName}</h1>
          <p>{courseInfo["description"]}</p>
          <Row>
            <Col md>
              <h5>Prerequisites</h5>
              <CourseLinks type={"prerequisites"} />
            </Col>
            <Col md>
              <h5>Corequisites</h5>
              <CourseLinks type={"co_requisites"} />
            </Col>
          </Row>
          <Row>
            <Col md>
              <h5>Exclusions</h5>
              <CourseLinks type={"exclusions"} />
            </Col>
            <Col md>
              <h5>Dependent Courses</h5>
              <CourseLinks type={"prerequisite_for"} />
            </Col>
          </Row>
        </Container>
      </React.Fragment>
    );
  } else return false;
};

// Place holder data fetcher
function tryFetchCourse(courseName) {
  if (courseName.length === 8) {
    const deptName = courseName.substring(0, 3);
    if (DATA.hasOwnProperty(deptName)) {
      const deptCourses = DATA[deptName];
      let re = new RegExp("^" + courseName);
      for (var key in deptCourses) {
        // return matching course info
        if (key.match(re)) return deptCourses[key];
      }
    }
  }
  return false;
}
