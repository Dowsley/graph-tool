import React, { useState } from 'react'
import Graph from 'react-graph-vis'
import axios from 'axios'

const App = () => {
  const [srcInput, setSrcInput] = useState('')
  const [destInput, setDestInput] = useState('')
  const [weightInput, setWeightInput] = useState('')

  const [srcAdjInput, setSrcAdjInput] = useState('')
  const [destAdjInput, setDestAdjInput] = useState('')

  const [srcDJInput, setSrcDJInput] = useState('')
  const [destDJInput, setDestDJInput] = useState('')
  
  const [weightedInput, setWeightedInput] = useState(false)
  const [directedInput, setDirectedInput] = useState(false)

  const [message, setMessage] = useState('')

  const [graphStructure,] = useState({
    weighted: false,
    directed: false,
    graph: null,
    order: null,
    size: null,
  })

  const [state, setState] = useState({
    graph: {
      nodes: [],
      edges: [],
    },
  })

  const renderGraphState = () => {
    const new_nodes = [...new Set(
      Object.keys(graphStructure.graph)
        .concat(
          Object
            .values(graphStructure.graph)
            .map((edges) => edges.map((e) => e[0]))
            .flat()
        )
    )].map(n => ({ id: n, label: n }))

    const new_edges = []
    Object.entries(graphStructure.graph)
      .forEach(([src, dests]) => {
        dests.forEach((dest) => {
          new_edges.push({ from: src, to: dest[0], weight: dest[1] })
        })
      })

    setState(({ graph: { nodes, edges }, ...rest }) => {
      return {
        graph: {
          nodes: [...new_nodes],
          edges: [...new_edges],
        },
        ...rest
      }
    })
  }

  const requestGraphChanges = (options) => {
    axios.post('http://127.0.0.1:5000', {
      state: graphStructure,
      changes: options,
    }).then((res) => {
      graphStructure.weighted = res.data.weighted
      graphStructure.directed = res.data.directed
      graphStructure.graph = res.data.graph
      graphStructure.order = res.data.order
      graphStructure.size = res.data.size

      renderGraphState()
    })
  }

  return (
    <>
      <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons" />
      <div className="flex">
        <div className="w-64 h-screen bg-white">
          <div className="flex items-center justify-center mt-10 font-bold text-4xl">
            GRAPH TOOL
          </div>

          <nav className="mt-10">
            <div className="flex mx-2 rounded-lg justify-between bg-gray-200 mt-5 py-2 px-6 space-x-3 text-gray-600 border-white hover:bg-gray-200 hover:text-gray-700 hover:border-gray-700">
              <div className="block">
                <div className="font-medium">
                  Ordem
                </div>
                <div className="flex justify-center font-bold text-3xl">
                  {graphStructure.order}
                </div>
              </div>

              <div className="block">
                <div className="font-medium">
                  Tamanho
                </div>
                <div className="flex justify-center font-bold text-3xl">
                  {graphStructure.size}
                </div>
              </div>
            </div>
            
            <div className="mx-2 rounded-lg flex items-center bg-gray-200 mt-5 py-2 px-6 space-x-3 text-gray-600 border-r-4 border-white hover:bg-gray-200 hover:text-gray-700 hover:border-gray-700">
              <div className="flex items-center space-x-1" >
                <button
                  className="flex bg-primary opacity-60 hover:opacity-100 rounded-full"
                  onClick={() => {
                    graphStructure.weighted = weightedInput
                    graphStructure.directed = directedInput
                    graphStructure.graph = null
                    graphStructure.order = null
                    graphStructure.size = null

                    setState(({ graph: { nodes, edges }, ...rest }) => {
                      return {
                        graph: {
                          nodes: [],
                          edges: [],
                        },
                        ...rest
                      }
                    })
                  }}
                >
                  <span className="material-icons" style={{ fontSize: '20px' }}>
                    add
                  </span>
                </button>
              </div>

              <div className="space-y-1">
                <div>
                  <span className="font-medium">
                    Criar novo grafo
                  </span>
                </div>

                <div className="space-x-1">
                  <input
                    name="Direcionado"
                    type="checkbox"
                    checked={directedInput}
                    onChange={() => setDirectedInput(!directedInput)}
                  />
                  <span>
                    Direcionado
                  </span>
                </div>

                <div className="space-x-1">
                  <input
                    name="Ponderado"
                    type="checkbox"
                    checked={weightedInput}
                    onChange={() => setWeightedInput(!weightedInput)}
                  />
                  <span>
                    Ponderado
                  </span>
                </div>
              </div>
            </div>

            <div className="mx-2 rounded-lg flex items-center bg-gray-200 mt-5 py-2 px-6 space-x-3 text-gray-600 border-r-4 border-white hover:bg-gray-200 hover:text-gray-700 hover:border-gray-700">
              <div className="flex items-center space-x-1" >
                <button
                  className="flex bg-primary opacity-60 hover:opacity-100 rounded-full"
                  onClick={() => {
                    requestGraphChanges({
                      new_edges: [
                        [[srcInput, destInput], weightedInput ? parseInt(weightInput) : null],
                      ],
                      adjacency: [],
                      get_degree: false,
                      get_adjacents: false,
                      dijkstra_table: false,
                    })
                  }}
                >
                  <span className="material-icons" style={{ fontSize: '20px' }}>
                    edit
                  </span>
                </button>
              </div>

              <div className="space-y-1">
                <span className="font-medium">
                  Adicionar Aresta
                </span>
                <input 
                  placeholder="Source"
                  value={srcInput}
                  onChange={(e) => setSrcInput(e.target.value)}
                />
                <input
                  placeholder="Destiny"
                  value={destInput}
                  onChange={(e) => setDestInput(e.target.value)}
                />
                <input
                  disabled={!weightedInput}
                  placeholder="Weight"
                  value={weightInput}
                  onChange={(e) => setWeightInput(e.target.value)}
                />
              </div>
            </div>

            <div className="mx-2 rounded-lg flex items-center bg-gray-200 mt-5 py-2 px-6 space-x-3 text-gray-600 border-r-4 border-white hover:bg-gray-200 hover:text-gray-700 hover:border-gray-700">
              <div className="flex items-center space-x-1" >
                <button
                  className="flex bg-primary opacity-60 hover:opacity-100 rounded-full"
                  onClick={() => {
                    axios.post('http://127.0.0.1:5000', {
                      state: graphStructure,
                      changes: {
                        new_edges: null,
                        adjacency: [srcAdjInput, destAdjInput],
                        get_degree: null,
                        get_adjacents: null,
                        dijkstra_table: false,
                      },
                    }).then((res) => {
                      const adjacency = res.data.adjacency

                      const string = adjacency
                        ? 'Sim :D'
                        : 'Não! >:('

                      setMessage(string)
                    })
                  }}
                >
                  <span className="material-icons" style={{ fontSize: '20px' }}>
                    close_fullscreen
                  </span>
                </button>
              </div>

              <div className="space-y-1">
                <span className="font-medium">
                  Checar Adjacência
                </span>
                <input 
                  placeholder="Source"
                  value={srcAdjInput}
                  onChange={(e) => setSrcAdjInput(e.target.value)}
                />
                <input
                  placeholder="Destiny"
                  value={destAdjInput}
                  onChange={(e) => setDestAdjInput(e.target.value)}
                />
                <div className="bg-green-300 px-2 py-2 rounded-lg">
                  {message}
                </div>
              </div>
            </div>

            <div className="mx-2 rounded-lg flex items-center bg-gray-200 mt-5 py-2 px-6 space-x-3 text-gray-600 border-r-4 border-white hover:bg-gray-200 hover:text-gray-700 hover:border-gray-700">
              <div className="flex items-center space-x-1" >
                <button
                  className="flex bg-primary opacity-60 hover:opacity-100 rounded-full"
                  onClick={() => {
                    axios.post('http://127.0.0.1:5000', {
                      state: graphStructure,
                      changes: {
                        new_edges: null,
                        adjacency: null,
                        get_degree: null,
                        get_adjacents: null,
                        dijkstra_table: srcDJInput,
                      },
                    }).then((res) => {
                      let dijkstraString = ''
                      
                      if (res.data.dijkstra_table[destDJInput]) {
                        // Requisito 3
                        dijkstraString += `O menor custo entre o vértice ${srcDJInput} e o vértice ${destDJInput} é de ${res.data.dijkstra_table[destDJInput][0]}\n`
                      
                        // Requisito 4
                        dijkstraString += '\n'
                        const path = [destDJInput]
                        let next = destDJInput
                        while (next !== srcDJInput) {
                          next = res.data.dijkstra_table[next][1]
                          path.push(next)
                        }
                        dijkstraString += `O caminho de menor custo entre o vértice ${srcDJInput} e o vértice ${destDJInput} é: ${path.reverse().join(' ->')}\n`
                      }
                      else {
                        dijkstraString += `NÃO TEM!!!!!!!\n`
                      }

                      alert(dijkstraString)
                    })
                  }}
                >
                  <span className="material-icons" style={{ fontSize: '20px' }}>
                    close_fullscreen
                  </span>
                </button>
              </div>

              <div className="space-y-1">
                <span className="font-medium">
                  Menor caminho
                </span>
                <input 
                  placeholder="Source"
                  value={srcDJInput}
                  onChange={(e) => setSrcDJInput(e.target.value)}
                />
                <input
                  placeholder="Destiny"
                  value={destDJInput}
                  onChange={(e) => setDestDJInput(e.target.value)}
                />
                <div className="bg-green-300 px-2 py-2 rounded-lg">
                  {message}
                </div>
              </div>

              
            </div>

          </nav>
        </div>

          <div style={{
            width: 1000,
            height: 1000
          }}>
            <Graph
              graph={state.graph}
              options={{
                layout: {
                  hierarchical: false
                },
                edges: {
                  color: "#000000"
                }
              }}
              events={{
                select: ({ nodes, edges }) => {
                  if (!nodes.length) {
                    return
                  }
          
                  const vertex = nodes[0]
          
                  axios.post('http://127.0.0.1:5000', {
                    state: graphStructure,
                    changes: {
                      new_edges: null,
                      adjacency: null,
                      get_degree: vertex,
                      get_adjacents: vertex,
                      dijkstra_table: vertex,
                    },
                  }).then((res) => {
                    const degree = res.data.degree
                    const adjacents = res.data.adjacents
          
                    let degreeString = ''
                    let adjacentString = ''
                    let dijkstraString = ''

                    if (directedInput) {
                      degreeString += `O grau ingoing do vértice ${vertex} é: ${degree[0]}\n`
                      degreeString += `O grau outgoing do vértice ${vertex} é: ${degree[1]}\n`
          
                      adjacentString += `Os adjacentes ingoing deste vértice são: ${adjacents[0].toString()}\n`
                      adjacentString += `Os adjacentes outgoing deste vértice são: ${adjacents[1].toString()}\n`
                    } else {
                      degreeString += `O grau do vértice ${vertex} é: ${degree[0]}\n`
                      adjacentString += `Os adjacentes deste vértice são: ${adjacents[0].toString()}\n`
                    }
                    
                    // Requisito 1
                    dijkstraString += '\n'
                    Object.entries(res.data.dijkstra_table).forEach(([k, v]) => {
                      dijkstraString += `O menor custo entre o vértice ${vertex} e o vértice ${k} é de ${v[0]}\n`
                    })
                    
                    // Requisito 2
                    dijkstraString += '\n'
                    const entries = Object.entries(res.data.dijkstra_table).filter(([goal]) => goal !== vertex)
                    entries.forEach(([goal, v]) => {
                      const path = [goal]

                      let next = goal
                      while (next !== vertex) {
                        next = res.data.dijkstra_table[next][1]
                        path.push(next)
                      }
                      dijkstraString += `O caminho de menor custo entre o vértice ${vertex} e o vértice ${goal} é: ${path.reverse().join(' ->')}\n`
                    })
          
                    alert(degreeString + adjacentString + dijkstraString)
                  })
                }
              }}
            />
          </div>
        </div>
    </>
  );

}

export default App
