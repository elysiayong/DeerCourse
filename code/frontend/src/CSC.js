import React from 'react'
import { Container, Row, Col } from 'react-bootstrap'
import { Content } from './components/StyledComponents'
import DATA from './components/program_data.json';   // Temporary course info "database"

export const CSC = () => {

    // Place holder until web scraper is connected.
    let courses = createCourseList();

    let leftCourses = courses.map((course, idx) => (
        <div className='App-container' key={idx}>
            <a className='App-link' href={"/course/" + course.substring(0, 8)}>{course}</a>
            <br />
        </div >
    ));

    return (
        <Content>
            <h1>Computer Science</h1>
            <h2>List of Courses</h2>
            {/* Refactor this part of the code. 
                Compartamentalize the container into a different file once
                final design decision has been made.
            */}
            <Container>
                <Row>
                    <Col>
                        {leftCourses}
                    </Col>
                </Row>
            </Container>
        </Content>
    )

    // Pull information from temporary JSON file
    function createCourseList() {
        let courses = [], course;
        for (course in DATA.CSC) {
            courses.push(course);
        }
        return courses;
    }
}
