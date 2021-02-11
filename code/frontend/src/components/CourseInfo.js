import React from 'react';
import { Jumbotron, Container } from 'react-bootstrap';
import DATA from './program_data.json';   // Temporary course info "database"


export function CourseInfo(props) {
    const courseName = props.courseName;
    const courseInfo = tryFetchCourse(courseName);
    if (courseInfo) {
        return (
            <React.Fragment>
                <Jumbotron fluid>
                    <Container>
                        <h1>{courseName}</h1>
                        <p>{courseInfo['description']}</p>
                    </Container>
                </Jumbotron>
            </React.Fragment>
        );
    } else return false;

}

// Place holder data fetcher
function tryFetchCourse(courseName) {
    if (courseName.length > 6) {
        const deptName = courseName.substring(0, 3);
        if (DATA.hasOwnProperty(deptName)) {
            const deptCourses = DATA[department];
            let re = new RegExp("^" + courseName);
            for (key in deptCourses) {
                // return matching course info
                if (key.match(re)) return deptCourses[key];
            }
        }
    }
    return false;
}