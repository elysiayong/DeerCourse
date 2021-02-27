import styles from './Bookmarks.module.css';
import React from 'react';
import { Container, Accordion, Card, Button } from 'react-bootstrap';
import { Content } from './components/StyledComponents';
import DATA from './components/program_data.json';   // Temporary course info "database"

export const Bookmarks = () => {

  let courses = createCourseList();

  let bookmarks = courses.map((course, idx) => 
  {
    let info = DATA.CSC[course]
    return (
      <Card key={idx} >
        <Card.Header >
          <Accordion.Toggle as={Button} className={styles.bookmarkCard} variant="link" eventKey={idx+1}>
            {course}
          </Accordion.Toggle>
        </Card.Header>
        <Accordion.Collapse eventKey={idx+1}>
          <Card.Body className={styles.bookmarkBody}>
            <h4>Description</h4> 
            <div className={styles.bookmarkDescription}>{info.description}</div>

            <h4>Exclusions</h4> 
            <div className={styles.bookmarkDescription}>{info.exclusions}</div>

            <h4>Prerequisites</h4> 
            <div className={styles.bookmarkDescription}>{info.prerequisites === "" ? 'None' : info.prerequisites}</div>

            <h4>Co-Requisites</h4> 
            <div className={styles.bookmarkDescription}>{info.co_requisites === "" ? 'None' : info.co_requisites}</div>

            <h4>Prerequisites For</h4> 
            <div className={styles.bookmarkDescription}>{info.prerequisite_for.length === 0 ? 'None' : info.prerequisite_for.join(", ")}</div>
          </Card.Body>
        </Accordion.Collapse>
      </Card>
    )
  });

  return (
    <Content>

      <h1>My Bookmarks</h1>

      <Container >
        <Accordion>
          {bookmarks}
        </Accordion>
      </Container>
    </Content>
  )
  
  // Pull information from temporary JSON file
  // Ignore the spaghetti code pls
  function createCourseList() {

    let courses = [], course, stop = 0;
    for (course in DATA.CSC) {
       courses.push(course);
       if (stop === 4) {
         return courses;
       }
       stop++;
     }
    return courses;
  }
}
