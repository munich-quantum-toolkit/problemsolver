
import React from 'react';

interface PathPosIsProps {
    path: number;
    position: number;
    vertex: string;
    onClick?: (path: number, position: number, vertex: string) => void;
}

const PathPosIs: React.FC<PathPosIsProps> = ({ path, position, vertex, onClick }) => {
    return (
        <div onClick={() => onClick?.(path, position, vertex)} className={`justify-around inline-flex flex-wrap-nowrap text-center border-2 rounded p-1 ${onClick !== undefined ? "cursor-pointer" : ""}`}>
            <span>Path</span>
            <span>{path}</span>
            <span>position</span>
            <span>{position}</span>
            <span>is: </span>
            <span>{vertex}</span>
        </div>
    );
};

export default PathPosIs;
