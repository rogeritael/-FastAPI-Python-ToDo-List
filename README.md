# FastAPI - Python ToDo List

## Registrar Tarefa [POST] [PARAM task]
```cmd
    /register
```
<span>
    {
        "task": "Arrumar o quarto",
        "isDone": false
    }
</span>

</br></br>

## Recuperar tarefas [POST] [PARAMS - option: int]
```cmd
    /task
```
<span><strong>option 0<strong> recupera todas as tarefas<span>
<span><strong>option 1<strong> recupera as tarefas que ainda não foram realizadas<span>
<span><strong>option 2<strong> recupera as tarefas realizadas<span>

</br></br>

## Buscar Tarefa pelo ID [GET]
```cmd
    /task/{id}
```

</br></br>

## Editar Tarefa [PUT] [PARAM task]
```cmd
    /task/{id}
```
<span>
    {
        "task": "Arrumar o quarto",
        "isDone": false
    }
</span>

</br></br>

## Excluir Tarefa [DELETE]
```cmd
    /task/{id}
```
