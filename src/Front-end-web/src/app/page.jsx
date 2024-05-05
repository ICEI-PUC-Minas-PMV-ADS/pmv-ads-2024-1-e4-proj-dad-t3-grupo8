'use client'
import ClassList from "@/components/class-list";
import Mural from "@/components/mural";
import { Button } from "@/components/ui/button";
import Link from "next/link";

export default function Home() { 

  return (
    <div className="w-full h-full flex flex-col justify-center items-center gap-10">
      <Link href="/cadastro/turma"> <Button> Cadastrar Nova Turma </Button> </Link>
      <div className="flex">
        <ClassList />
        <Mural />
      </div>
    </div>
  );
}
