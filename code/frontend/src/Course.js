import React from 'react'
import { CourseInfo } from './components/CourseInfo';
import { Redirect, useParams } from 'react-router-dom';
import { Content } from './components/StyledComponents'

export function CoursePage() {
    let { courseName } = useParams();
    const courseDisplay = CourseInfo(courseName);
    if (courseDisplay) {
        return (
            <Content>
                {courseDisplay}
            </Content>
        );
    } else {
        return <Redirect to="/404" />;
    }
}

