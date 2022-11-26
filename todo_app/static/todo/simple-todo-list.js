const todo = {
  action(e) {
    const target = e.target;
    if (target.classList.contains('todo__action')) {
      const action = target.dataset.todoAction;
      const elemItem = target.closest('.todo__item');
      if (action === 'deleted' && elemItem.dataset.todoState === 'deleted') {
        elemItem.remove();
      } else {
        elemItem.dataset.todoState = action;
        const lexicon = {
          active: 'восстановлено',
          completed: 'завершено',
          deleted: 'удалено'
        };
        const elTodoDate = elemItem.querySelector('.todo__date');
        const html = `<span>${lexicon[action]}: ${new Date().toLocaleString().slice(0, -3)}</span>`;
        elTodoDate.innerHTML = html;
      }
      this.save();
    } else if (target.classList.contains('todo__add')) {
      this.add();
      this.save();
    }
  },
  add() {
    const elemText = document.querySelector('.todo__text');
    if (elemText.disabled || !elemText.value.length) {
      return;
    }
    document.querySelector('.todo__items').insertAdjacentHTML('beforeend', this.create(elemText.value));
    elemText.value = '';
    document.dispatchEvent(new Event('todo-item-add'));
  },

  

  create(text) {
    const date = JSON.stringify({ add: new Date().toLocaleString().slice(0, -3) });
    return `<li class="todo__item" data-todo-state="active">
      <span class="todo__task">
        <p>${text}</p>
        <p><textarea id="com" placeholder = "Описание"></textarea></p>
        <p><textarea id="com1" placeholder = "О"></textarea></p>
        <span class="todo__date" data-todo-date="${date}">
          <span>добавлено: ${new Date().toLocaleString().slice(0, -3)}</span>
        </span>
         <input type="checkbox" class="custom-checkbox" id="happy" name="happy" value="yes">
          <label for="happy">Задача не выполнена в срок</label>
        </span>
        <div class="overlay">

        <div id="alarm-dialog">

            <h2>Set alarm after</h2>

        <label class="hours">
            Hours
            <input type="number" value="0" min="0" />
        </label>

        <p><label class="minutes">
            Minutes
            <input type="number" value="0" min="0" />
        </label></p>

        <p><label class="seconds">
            Seconds
            <input type="number" value="0" min="0" />
        </label></p>

        <div class="button-holder">
            <a id="alarm-set" class="button blue">Set</a>
            <a id="alarm-clear" class="button red">Clear</a>
        </div>

            <a class="close"></a>

        </div>

    </div>

    <div class="overlay">

        <div id="time-is-up">

           <h2>Time's up!</h2>

           <div class="button-holder">
                <a class="button blue">Close</a>
           </div>

        </div>
    </div>
      <span class="todo__action todo__action_restore" data-todo-action="active"></span>
      <span class="todo__action todo__action_complete" data-todo-action="completed"></span>
      <span class="todo__action todo__action_delete" data-todo-action="deleted"></span></li>`;
  },




  init() {
    const fromStorage = localStorage.getItem('todo');
    if (fromStorage) {
      document.querySelector('.todo__items').innerHTML = fromStorage;
    }
    document.querySelector('.todo__options').addEventListener('change', this.update);
    document.addEventListener('click', this.action.bind(this));
  },
  update() {
    const option = document.querySelector('.todo__options').value;
    document.querySelector('.todo__items').dataset.todoOption = option;
    document.querySelector('.todo__text').disabled = option !== 'active';
  },
  save() {
    localStorage.setItem('todo', document.querySelector('.todo__items').innerHTML);
  }
};

document.addEventListener("DOMContentLoaded", function() { // событие загрузки страницы

    // выбираем на странице все элементы типа textarea и input
    document.querySelectorAll('textarea').forEach(function(e) {
        // если данные значения уже записаны в sessionStorage, то вставляем их в поля формы
        // путём этого мы как раз берём данные из памяти браузера, если страница была случайно перезагружена
        if(e.value === '') e.value = window.sessionStorage.getItem(e.name, e.value);
        // на событие ввода данных (включая вставку с помощью мыши) вешаем обработчик
        e.addEventListener('input', function() {
            // и записываем в sessionStorage данные, в качестве имени используя атрибут name поля элемента ввода
            window.sessionStorage.setItem(e.name, e.value);
        })
    })

}); 

todo.init();