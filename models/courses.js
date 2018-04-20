var uiModels = uiModels || {};

uiModels.courses = {
  id: 'courses',
  label: 'Course',
  icon: 'contact.gif',
  name: 'course', namePlural: 'courses',
  fnTitle: function (model) {
    return model.get('title');
  },
  fnSearch: ['title', 'description'],
  elements: [
    {
      type: 'panel', label: 'Title', width: 62,
      elements: [
        {
          id: 'title', attribute: 'title', type: 'text', label: 'Title', required: true,
          //placeholder: 'Title of the course',
          maxLength: 255,
          width: 100, inMany: true
        }
      ]
    },
    {
      type: 'panel', label: 'Evaluation', width: 38,
      elements: [
        {
          id: 'done', attribute: 'done', type: 'boolean', width: 100, inMany: true,
          label: 'Done',
          labelCharts: 'Evaluation Complete', labelTrue: 'Complete', labelFalse: 'Incomplete',
          typeChart: 'pie'
        }
      ]
    },
    {
      type: 'panel', label: 'Course Description', label2: 'and notes', width: 100,
      elements: [
        {
          id: 'description', attribute: 'description', type: 'textmultiline',
          label: 'Description', maxLength: 1000,
          width: 100, height: 6, inMany: false
        }
      ]
    }
  ]
};

if (typeof module === "object" && typeof module.exports === "object") {
  module.exports = uiModels.courses;
}
