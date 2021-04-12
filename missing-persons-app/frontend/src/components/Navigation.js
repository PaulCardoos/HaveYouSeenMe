import React from 'react'
import { Navbar, Button, Nav,FormControl, Form } from 'react-bootstrap'


const Navigation = () => {
    return (
        <div>
            <Navbar className='mb-4' bg="light" expand="lg">
                <Navbar.Brand href="#home">Missing Person App</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="mr-auto">
                        <Nav.Link href="/">Home</Nav.Link>
                        <Nav.Link href="/report">Report</Nav.Link>
                        <Nav.Link href="/stats">Stats</Nav.Link>
                    </Nav>
                    <Form inline>
                        <FormControl type="text" placeholder="Search" className="mr-sm-2" />
                        <Button variant="outline-success">Search</Button>
                    </Form>
                </Navbar.Collapse>
            </Navbar>
        </div>
    )
}

export default Navigation
