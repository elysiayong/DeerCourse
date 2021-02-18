import React from 'react'
import { CourseInfo } from './components/CourseInfo';
import { Redirect, useParams } from 'react-router-dom';

export function CoursePage() {
    let { courseName } = useParams();
    const courseDisplay = CourseInfo(courseName);
    if (courseDisplay) {
        return (
            <React.Fragment>
                {courseDisplay}
            </React.Fragment>
        );
    } else {
        return <Redirect to="/404" />;
    }
}

