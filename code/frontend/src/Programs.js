import React from 'react'
import { Container, Row, Col } from 'react-bootstrap'
import { Content } from './components/StyledComponents'

export const Programs = () => {

    /* Added as a place holder until web scraper is connected.
     */
    let programsLeft = ['Antrhopology',
        'Astronomy',
        'Biology',
        'Biomedical Communications',
        'Chemistry',
        'Cinema Studies',
        'Classical Civilization',
        'Communications, Culture, Information, and Technology',
        'Computer Science',
        'Concurrent Teacher Education',
        'Criminology, Law and Society',
        'Diaspora and Transnational Studies',
        'Drama',
        'Earth Science',
        'Economics',
        'Education Studies',
        'English',
        'Environment',
        'Environmental Geoscience',
        'Fine Art History (FAH)',
        'Fine Art Studio (FAS)',
        'Forensic Science'
    ]
    
    let programsRight = ['French',
        'Geography',
        'History',
        'History of Religion',
        'Institute for Management and Innovation',
        'Institute for the Stude of University Pedagogy (ISUP)',
        'Italian',
        'Language Studies',
        'Language Teacher and Learning: French and Italian (HBA)',
        'Linguistics',
        'Managament',
        'Mathematics',
        'Philosophy',
        'Physics',
        'Political Science',
        'Psychology',
        'Sociology',
        'South Asian Humanities',
        'Statistics',
        'Visual Culture and Communication',
        'Woman and Gender Studies'
    ]

    let leftPrograms = createColumn(programsLeft);
    let rightPrograms = createColumn(programsRight);

    return (
        <Content>
            <h1>Programs</h1>
            {/* Refactor this part of the code. 
                Compartamentalize the container into a different file once
                final design decision has been made.
            */}
            <Container>
                <Row>
                    <Col>
                        {leftPrograms}
                    </Col>
                    <Col>
                        {rightPrograms}
                    </Col>
                </Row>
            </Container>
        </Content>
    )

    function createColumn(programList) {
        return programList.map((program, idx) => (
            <div className='App-container' key={idx}>
                <a className='App-link' href={"/course/" + program.substring(0, 8)}>{program}</a>
                <br />
            </div >
        ));
    }
}
