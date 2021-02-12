import React from 'react'
import './App.css'

import {Container, Row, Col, Alert} from 'react-bootstrap'

import bg from './assets/bg-image2.jpg'
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
  justify-content: center;
  width: 100%;
  height:100%;
  background-attachment: fixed;
`


export const CSC = () => {
    
    let courses = [ 'CSC104H5 The Why and How of Computing',
                    'CSC108H5 Introduction to Computer Programming',
                    'CSC148H5 Introduction to Computer Science',
                    'CSC199H5 Computer Science Seminar',
                    'CSC207H5 Software Designy',
                    'CSC209H5 Software Tools and Systems Programming',
                    'CSC236H5 Introduction to the Theory of Computation ',
                    'CSC258H5 Computer Organization',
                    'CSC263H5 Data Structures and Analysis',
                    'CSC290H5 Communication Skills for Computer Scientists',
                    'CSC299Y5 Research Opportunity Program',
                    'CSC300H5 Computers and Society',
                    'CSC301H5 Introduction to Software Engineering',
                    'CSC309H5 Programming on the Web',
                    'CSC310H5 Information Theory',
                    'CSC311H5 Introduction to Machine Learning',
                    'CSC318H5 The Design of Interactive Computational Media',
                    'CSC320H5 Introduction to Visual Computing',
                    'CSC322H5 Introduction to Algebraic Cryptography',
                    'CSC324H5 Principles of Programming Languages',
                    'CSC333H5 Forensic Computing',
                    '...'
                  ]

    
    let leftCourses = courses.map((courses, idx) => (

                                <Alert className='App-link-container' key={idx}>
                                    <Alert.Link className='App-link' href="#">{courses}</Alert.Link>
                                </Alert>));

    return(
        <React.Fragment>
            <Background>   
                <br></br>
                <h1>Computer Science</h1>
                <Container>
                    <Row>
                        <Col>
                            {leftCourses}
                        </Col>
                    </Row>           
                </Container> 
            </Background>
        </React.Fragment>
    )
}