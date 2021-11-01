import * as React from 'react';
import {Box, Table, TableContainer, Paper, TableBody, Button, TextField} from '@material-ui/core';
import Tablerow from '../components/table'
import ModalEdit from '../components/modal_edit'
import ModalNew from '../components/modal_new'
import ModalEditSocket from '../components/modal_edit_socket'
import ModalNewSocket from '../components/modal_new_socket'
import Stack from '@mui/material/Stack';
import {apiTaskAll, apiTaskDelete, apiTaskAdd, apiTaskRename, apiTaskCheck} from "../api/api";


export default class Todolist extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            data: [],
            socket: new WebSocket(`ws://localhost:8000/ws/get/`),
            notes: [],
        };
    }

    componentDidMount() {

        apiTaskAll().then(response => {
            try {
                const data1 = response.data;
                this.setState({data: data1})

            } catch (err) {
                console.log('eeeeror')
            }
        });

        this.state.socket.onmessage = e => {
            const data1 = JSON.parse(e.data);

            this.setState({notes: data1})
            console.log(this.state.notes.data)
        }


    }

//////// Http Handl
    handleChange = (id, name, checked) => {
        let data1 = this.state.data;
        const index = data1.findIndex(x => x.id === id)
        data1[index].name = name;
        this.setState({data: data1});
        apiTaskRename(id, name, checked)
    };

    checkFunction = (id) => {
        let data1 = this.state.data;
        const index = data1.findIndex(x => x.id === id)
        data1[index].checked = !data1[index].checked;
        this.setState({data: data1});
        apiTaskCheck(id, data1[index].checked)

    };

    handldelete = (id) => {
        let data1 = this.state.data;
        data1 = data1.filter(data1 => data1.id !== id)
        this.setState({data: data1});
        apiTaskDelete(id)
    }
    handladd = (name) => {
        apiTaskAdd(name, false)
        this.componentDidMount()
    }

//////// socket handl
    socketchange = (id, text) => {
        try {
            let temp = this.state.notes;
            const index = temp.findIndex(x => x.id === id)
            temp[index].text = text;
            this.setState({notes: temp});

            this.state.socket.send(JSON.stringify({
                'header':"PUT",
                'id': id,
                'text':text,
              }));

        } catch (_) {
            console.log("error")
        }

    }

    socketdelete = (id) => {
        let temp = this.state.notes;
        temp = temp.filter(temp => temp.id !== id)
        this.setState({notes: temp});
        this.state.socket.send(JSON.stringify({
            'header':"DELETE",
            'id': id,
        }));
    }
    socketadd = (text) => {
        this.state.socket.send(JSON.stringify({
            'header':"POST",
            'text':text,
        }));
        this.componentDidMount()


    }

    render() {
        return (

            <div>

                <h1 style={{marginLeft: 540}}>My TODO list</h1>
                <TableContainer component={Paper}>
                    <Table sx={{minWidth: 850}} size="norm" aria-label="a dense table">
                        <TableBody>
                            {this.state.data.map((row) => (
                                <Stack direction="row" spacing={3}>
                                    <Tablerow
                                        checkFunction={this.checkFunction}
                                        name={row.name}
                                        checked={row.checked}
                                        id={row.id}
                                    />
                                    <ModalEdit
                                        handleChange={this.handleChange}
                                        id={row.id}
                                        checked={row.checked}

                                    />
                                    <Button
                                        variant="contained"
                                        style={{marginLeft: "auto"}}
                                        onClick={() => {
                                            this.handldelete(row.id);
                                        }}
                                    >
                                        Удалить
                                    </Button>
                                </Stack>
                            ))}
                        </TableBody>
                    </Table>
                </TableContainer>
                <ModalNew

                    handleChange={this.handladd}
                />
                <br/>
                <Stack direction="column" spacing={2}>
                    <h1 style={{marginLeft: 540}}>Заметки</h1>
                    {this.state.notes.map((row) => (
                        <Stack direction="row">
                        <textarea
                            style={{resize: "none", height: 50, width: 1000}}
                            value={row.text}
                        />

                            <ModalEditSocket
                                socketchange={this.socketchange}
                                id={row.id}
                            />

                            <Button
                                variant="contained"
                                style={{marginLeft: "auto"}}
                                onClick={() => {
                                    this.socketdelete(row.id)
                                }}
                            >
                                Удалить
                            </Button>
                        </Stack>
                    ))}
                    <ModalNewSocket

                        handleChange={this.socketadd}
                    />
                </Stack>
            </div>
        );
    }
};