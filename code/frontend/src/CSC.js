import React from 'react'
import { Container, Row, Col } from 'react-bootstrap'
import { Content } from './components/StyledComponents'

export const CSC = () => {

    /* Added as a place holder until web scraper is connected.
     */
    let courses = ['CSC104H5 The Why and How of Computing',
        'CSC108H5 Introduction to Computer Programming',
        'CSC148H5 Introduction to Computer Science',
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

    let leftCourses = courses.map((course, idx) => (
        <React.Fragment className='App-container' key={idx}>
            <a className='App-link' href={"/course/" + course.substring(0, 8)}>{course}</a>
            <br />
        </React.Fragment >
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
}