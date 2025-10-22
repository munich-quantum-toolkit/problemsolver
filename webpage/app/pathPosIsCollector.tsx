import React, { useState } from 'react';
import Toggle from './toggle';
import PathPosIs from './pathPosIs';

interface PathPosIsCollectorProps {
    title: string;
    cols?: number;
    allVertices: string[];
    nPaths: number;
    pathLength: number;
    onChange?: (items: string[][]) => void;
}

const PathPosIsCollector: React.FC<PathPosIsCollectorProps> = ({ title, cols = 2, allVertices, nPaths, pathLength, onChange}) => {
    // Component logic goes here
    const [items, setItems] = useState<string[][]>([]);

    const itemAdded = (path: string, position: string, vertex: string) => {
        if(vertex === "")
            return;
        if(items.some((item) => item[0] == path && item[1] == position && item[2] == vertex))
            return;
        const newItems = [...items];
        newItems.push([path, position, vertex]);
        setItems(newItems);
        onChange?.(newItems);
    }

    const itemRemoved = (path: string, position: string, vertex: string) => {
        const newItems = [...items];
        newItems.splice(newItems.findIndex((item) => item[0] == path && item[1] == position && item[2] == vertex), 1);
        setItems(newItems);
        onChange?.(newItems);
    }

    const pathRef = React.createRef<HTMLSelectElement>();
    const posRef = React.createRef<HTMLSelectElement>();
    const vertexRef = React.createRef<HTMLSelectElement>();

    return (
        // JSX markup goes here
        <div>
            <h1>{title}</h1>
            <div className='flex flex-row gap-4 mb-2'>
                <span className="pb-1 pt-1">Path</span>
                <select ref={pathRef} className="border-2 rounded p-1">
                    {
                        (new Array(nPaths).fill(0)).map((_, index) => (
                            <option key={index}>{index + 1}</option>
                        ))
                    }
                </select>
                <span className="pb-1 pt-1">position</span>
                <select ref={posRef} className="border-2 rounded p-1">
                    {
                        (new Array(pathLength).fill(0)).map((_, index) => (
                            <option key={index}>{index + 1}</option>
                        ))
                    }
                </select>
                <span className="pb-1 pt-1">is</span>
                <select ref={vertexRef} className="border-2 rounded p-1">
                    {
                        allVertices.map((vertex, index) => (
                            <option key={index}>{vertex}</option>
                        ))
                    }
                </select>
                <button className='border-2 rounded bg-slate-100 p-1 hover:bg-slate-200 active:bg-slate-300'
                    onClick={() => itemAdded(pathRef.current?.value ?? "", posRef.current?.value ?? "", vertexRef.current?.value ?? "")}>Add</button>
            </div>
            <div className={`grid grid-cols-${cols} gap-4`}>
                {
                    items.map((item, index) => (
                        <PathPosIs
                            onClick={(path, position, vertex) => itemRemoved?.(path + "", position + "", vertex)}
                            path={parseInt(item[0])}
                            position={parseInt(item[1])}
                            vertex={item[2]}
                            key={index}>
                        </PathPosIs>
                    ))
                }
            </div>
        </div>
    );
};

export default PathPosIsCollector;
