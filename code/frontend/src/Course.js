import React from 'react'
import { CourseInfo } from './components/CourseInfo';
import { Redirect, useParams } from 'react-router-dom';
import bg from './assets/bg-image2.jpg';
import styled from 'styled-components';

/* style from https://www.youtube.com/watch?v=f8Up35TVNgo&feature=share&ab_channel=JoeBenjamin*/
const Background = styled.div`
  background-image: url(${bg});
  background-position: left;
  background-size: cover;
  background-repeat: no-repeat;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  height:100vh;
`

export function CoursePage() {
    let { courseName } = useParams();
    const courseDisplay = CourseInfo(courseName);
    if (courseDisplay) {
        return (
            <React.Fragment>
                <Background>
                    {courseDisplay}
                </Background>
            </React.Fragment>
        );
    } else {
        return <Redirect to="/404" />;
    }
}

