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
    
    let courses = [ 'CSC104 The Why and How of Computing',
                    'CSC108  Introduction to Computer Programming',
                    'CSC148 Introduction to Computer Science',
                    'CSC199H5 Computer Science Seminar',
                    'CSC207H5 Software Design',
                    'CSC209H5 Software Tools and Systems Programming',
                    'CSC236H5 Introduction to the Theory of Computation',
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
                    'CSC338H5 Numerical Methods',
                    'CSC343H5 Introduction to Databases',
                    'CSC347H5 Introduction to Information Security',
                    'CSC358H5 Principles of Computer Networks',
                    'CSC363H5 Computational Complexity and Computability',
                    'CSC367H5 Parallel Programming',
                    'CSC369H5 Operating Systems',
                    'CSC373H5 Algorithm Design and Analysis',
                    'CSC375H5 Programming Mechatronic Systems',
                    'CSC376H5 Fundamentals of Robotics',
                    'CSC384H5 Introduction to Artificial Intelligence',
                    'CSC392H5 Computer Science Implementation Project',
                    'CSC393h5 Computer Science Expository Work',
                    'CSC398H5 Topics in Computer Science',
                    'CSC399Y5 Research Opportunity Program',
                    'CSC404H5 Video Game Design',
                    'CSC409H5 Scalable Computing',
                    'CSC413H5 Neural Networks and Deep Learning',
                    'CSC420H5 Introduction to Image Understanding',
                    'CSC422H5 Cryptography and Computational Complexity',
                    'CSC423H5 Computer Forensics',
                    'CSC427H5 Computer Security',
                    'CSC428H5 Human-Computer Interaction (SCI)',
                    'CSC448H5 Formal Languages and Automata',
                    'CSC458H5 Computer Networks',
                    'CSC469H5 Operating Systems Design and Implementation',
                    'CSC476H5 Continuum Robotics',
                    'CSC477H5 Introduction to Mobile Robotics',
                    'CBJ481Y5 Independent Project in Bioinformatics',
                    'CSC488H5 Compilers and Interpreters',
                    'CSC490H5 Capstone Design Course',
                    'CSC492H5 Computer Science Implementation Project',
                    'CSC493H5 Computer Science Expository Work',
                    'CSC497H5 Topics in Computer Science',
                    'CSC498H5 Topics in Computer Science',
                    'CSC499Y5 Research Opportunity Program'
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