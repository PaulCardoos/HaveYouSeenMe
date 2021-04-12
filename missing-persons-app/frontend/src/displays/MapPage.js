import React from 'react'
import USA from 'react-usa-map'
import { Container, Row, Col } from 'react-bootstrap'
import axios from 'axios'


const MapPage = () => {

    const mapHandler = async (e) => {
        let state = e.target.dataset.name
        const {data} = await axios.get(`http://localhost:5005/api/v1/search/${state}`)
        console.log(data)
    }

    return (
        <Container>
            <Row className='d-flex justify-content-center'>
                <Col className='justify-content-center' lg={8} md={12} sm={12}>
                    <USA width="100%" height="100%" onClick={(e) => mapHandler(e)}/>
                </Col>
                <Col lg={4} md={12} sm={12}>
                </Col>
            </Row>
        </Container>
    )
}

export default MapPage
