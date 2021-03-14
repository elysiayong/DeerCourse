
import React from "react";
import { Row, Col, Container } from "react-bootstrap";
import { Content } from '../StyledComponents'
import "./ReviewComponent.css"
import logo from '../../assets/deer.png';


export const ReviewComponent = () => {

	const Review = ({date, comment, usefulness, year, major}) =>
	(
		<Container className='reviewContainer'>
			<Row>
				<Col xs={3} className='studentInfo'>
					<h4>Student Information</h4>
					<img src={logo} width="100%" alt='Deer Logo Place Holder Profile'/>
					<p>{major}</p>
					<p>{year} year</p>
				</Col>
				
				<Col className="reviewInfo">
					<Row >
						Posted on {date}
					</Row>
					<Row >
						<h3>{comment}</h3>
					</Row>
					<Row>
						<p>{usefulness} found this review helpful</p>
					</Row>
					
				</Col>
			</Row>
		</Container>
	);

	return (
		<Content>
			<h1>Reviews</h1>
			<Review date="26 January 2021" comment="Very easy birdcourse for first years!! Must take!!" usefulness="-999" year="4th" major="Math Specialist" />
			<Review date="12 March 2021" comment="Too difficult :(" usefulness="100" year="1st" major="Computer Science Major" />
			
		</Content>
	)
};
