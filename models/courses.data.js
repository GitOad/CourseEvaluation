var uiModels = uiModels || {};
uiModels.courses_data = [{
  id: 1,
  title: 'Software Architecture',
  description: 'Software architecture refers to the high level structures of a software system, the discipline of creating such structures, and the documentation of these structures.',
  done: false
}, {
  id: 2,
  title: 'Software Management',
  description: 'Software project management is an art and science of planning and leading software projects.',
  done: true
}];

if (typeof module === "object" && typeof module.exports === "object") {
  module.exports = uiModels.courses_data;
}
