import React from 'react';
import { Container, Row, Col } from 'react-bootstrap';
import { Link } from "react-router-dom";
import DATA from './program_data.json';   // Temporary course info "database"

export function CourseInfo(courseName) {
    const courseInfo = tryFetchCourse(courseName);
    if (courseInfo) {
        return (
            <React.Fragment>
                <Container>
                    <h1>{courseName}</h1>
                    <p>{courseInfo['description']}</p>
                    <Row>
                        <Col md>
                            <h5>Prerequisites</h5>
                            <p>N/A</p>
                        </Col>
                        <Col md>
                            <h5>Corequisites</h5>
                            <p>N/A</p>
                        </Col>
                    </Row>
                    <Row>
                        <Col md>
                            <h5>Exclusions</h5>
                            <p>N/A</p>
                        </Col>
                        <Col md>
                            <h5>Dependent Courses</h5>
                            <p>
                                {courseInfo['prerequisite_for'].map((item, index) => {
                                    var link = <Link to={'/course/' + item}>{item}</Link>;
                                    return (
                                        <React.Fragment>{link} </React.Fragment>
                                    );
                                })}
                            </p>
                        </Col>
                    </Row>
                </Container>
            </React.Fragment>
        );
    } else return false;
}

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