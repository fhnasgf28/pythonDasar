angular.module('myApp', [])
  .component('myComponent', {
    template: `
      <h1>Hello, {{ $ctrl.name }}!</h1>
      <p>Welcome to {{ $ctrl.title }}</p>
    `,
    controller: function() {
      this.name = 'John Doe';
      this.title = 'Angular App';
    }
  });
