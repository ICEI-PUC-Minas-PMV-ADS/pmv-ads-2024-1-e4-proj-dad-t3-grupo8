'use client'
import { getClassList } from "@/hooks/tumas-hooks";
import { Avatar, AvatarImage } from "../ui/avatar";
import Link from "next/link";

const ClassList = () => {
    const {data} = getClassList();

    return (
        <div className="container grid grid-cols-classgrid gap-10 max-w-[1280px]"> 
                {data?.map(data => (
                    <Link 
                        key={data._id}
                        href={{ 
                            href:"/detalhes", 
                            query: {
                                id: `${data._id}`
                            }
                        }}
                    >
                        <div className="flex gap-5">
                            <Avatar className="w-[100px] h-[100px]">
                                <AvatarImage src="https://img.freepik.com/free-vector/empty-classroom-interior-with-chalkboard_1308-65378.jpg?size=626&ext=jpg&ga=GA1.1.1700460183.1713225600&semt=sph" />
                            </Avatar>
                            <div className="flex flex-col">
                                <p className="text-xl"> Turma {data.number}</p>
                                {data.students.length >= 1 && data.students.length != 0 
                                    ? <p className="text-slate-500 pb-5"> 1 Aluno </p>
                                    : <p className="text-slate-500 pb-5"> {data.students.length} Alunos </p>
                                }
                                <Link href="/" className="underline text-primaryPurple"> Cronograma de Aulas </Link>
                                <Link href="/" className="underline text-primaryPurple"> Mural </Link>
                            </div>
                        </div>
                    </Link>
                ))}
        </div>        
    )
}

export default ClassList;