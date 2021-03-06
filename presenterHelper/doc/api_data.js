define({ "api": [
  {
    "type": "post",
    "url": "git/create_presentation/",
    "title": "Request to create a presentation",
    "name": "CreatePresentation",
    "group": "Presentation",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>presentation name.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n   \"name\": \"presentation name\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "json",
            "optional": false,
            "field": "successMessage",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "json",
            "optional": false,
            "field": "201",
            "description": "<p>message presentation creation message</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "201 Success-Response:",
          "content": "{\n   'presentation_id': 2\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "json",
            "optional": false,
            "field": "404",
            "description": "<p>the User not found</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "./app/api_v1/presentation.py",
    "groupTitle": "Presentation"
  },
  {
    "type": "get",
    "url": "/get_all_presentations/",
    "title": "Request all presentations of a user",
    "name": "GetAllPresentations",
    "group": "Presentation",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "json",
            "optional": false,
            "field": "presentationList",
            "description": "<p>a list of presentations in json format</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "[{\"id\": 2, \"name\": \"software engineering\"}, {\"id\": 3, \"name\": \"pres1\"}]",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./app/api_v1/presentation.py",
    "groupTitle": "Presentation"
  },
  {
    "type": "get",
    "url": "/get_presentation/:id",
    "title": "Request Presentation with id",
    "name": "GetPresentation",
    "group": "Presentation",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>Presentation unique ID.</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "json",
            "optional": false,
            "field": "presentation",
            "description": "<p>presentation content provided in a json file</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "json",
            "optional": false,
            "field": "401",
            "description": "<p>unauthorized</p>"
          },
          {
            "group": "Error 4xx",
            "type": "json",
            "optional": false,
            "field": "404",
            "description": "<p>the presentation not found</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "401 Error-Response:",
          "content": "{\n   'error': 'unauthorized'\n}",
          "type": "json"
        },
        {
          "title": "404 Error-Response:",
          "content": "{\n   \"error\": \"the presentation not found\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./app/api_v1/presentation.py",
    "groupTitle": "Presentation"
  },
  {
    "type": "post",
    "url": "/create_session/",
    "title": "Request to create a session",
    "name": "CreateSession",
    "group": "Session",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Integer",
            "optional": false,
            "field": "pid",
            "description": "<p>presentation id.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n   \"pid\" : \"2\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "json",
            "optional": false,
            "field": "session_code",
            "description": "<p>session entrance code</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "200 Success-Response:",
          "content": "{\n   'session_code': 'W2GSA'\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "json",
            "optional": false,
            "field": "404",
            "description": "<p>the User not found</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "./app/api_v1/session.py",
    "groupTitle": "Session"
  },
  {
    "type": "Get",
    "url": "/get_sessions/uid",
    "title": "Request to get all sessions of a presenter",
    "name": "GetSessions",
    "group": "Session",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "uid",
            "description": "<p>presenter id.</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "201 Success-Response:",
          "content": "[{\"presentation_name\": \"computer\", \"code\": \"8X5XV\", \"name\": null, \"is_active\": true, \"current_page\": 0, \"end_date\": null}, {\"presentation_name\": \"photoshop\", \"code\": \"QSE9S\", \"name\": null, \"is_active\": true, \"current_page\": 0, \"end_date\": null,  \"participant_size\": 0}]",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "json",
            "optional": false,
            "field": "404",
            "description": "<p>the User not found</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "./app/api_v1/session.py",
    "groupTitle": "Session"
  },
  {
    "type": "post",
    "url": "/join_session/",
    "title": "Request to join a session",
    "name": "JoinSession",
    "group": "Session",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "code",
            "description": "<p>session code.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n   \"code\" : \"WX1RQ\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "json",
            "optional": false,
            "field": "201",
            "description": "<p>message session joined successfully</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "201 Success-Response:",
          "content": "{\n   'message': 'participant joined successfully'\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "json",
            "optional": false,
            "field": "404",
            "description": "<p>the User not found</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "./app/api_v1/session.py",
    "groupTitle": "Session"
  },
  {
    "type": "get",
    "url": "/forget-password/:email",
    "title": "respond to forget password request",
    "name": "ForgetPassword",
    "group": "User",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "json",
            "optional": false,
            "field": "201",
            "description": "<p>forgot message confirmation message</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "201 Success-Response:",
          "content": "{\n   'msg': 'change password link has been send to your email'\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "json",
            "optional": false,
            "field": "404",
            "description": "<p>user does not exist</p>"
          },
          {
            "group": "Error 4xx",
            "type": "json",
            "optional": false,
            "field": "406",
            "description": "<p>email did not send</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "404 Error-Response:",
          "content": "{\n   'error': 'this user does not exists'\n}",
          "type": "json"
        },
        {
          "title": "406 Error-Response:",
          "content": "{\n   'error': 'problem with sending email'\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./app/api_v1/users.py",
    "groupTitle": "User"
  },
  {
    "type": "get",
    "url": "/get-auth-token",
    "title": "authenticate in server",
    "name": "Log_in",
    "group": "User",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "username",
            "description": "<p>username</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "password",
            "description": "<p>password</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "token",
            "description": "<p>a long string is returned as a token</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\"token\": \"eyJhbGciOiJIUzI1NiIsImlhdCI6MTQ2\"}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "json",
            "optional": false,
            "field": "404",
            "description": "<p>userNotExist</p>"
          },
          {
            "group": "Error 4xx",
            "type": "json",
            "optional": false,
            "field": "403",
            "description": "<p>userNotVerified</p>"
          },
          {
            "group": "Error 4xx",
            "type": "json",
            "optional": false,
            "field": "400",
            "description": "<p>wrongPassword</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "404 Error-Response:",
          "content": "{\n   'error': 'userNotExist'\n   'message': 'please sign up'\n}",
          "type": "json"
        },
        {
          "title": "403 Error-Response:",
          "content": "{\n   'error': 'userNotVerified',\n   'message': 'please verify your email account'\n}",
          "type": "json"
        },
        {
          "title": "400 Error-Response:",
          "content": "{\n   'error': 'wrongPassword',\n   'message': 'The password is not correct'\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./app/__init__.py",
    "groupTitle": "User"
  },
  {
    "type": "post",
    "url": "/register",
    "title": "register a user",
    "name": "Register",
    "group": "User",
    "parameter": {
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n   \"email\": \"ehsanroman74@gmail.com\",\n   \"password\": \"asdfgh\",\n   \"firstname\": \"ehsan\",\n   \"lastname\": \"golshani\",\n   \"is_audience\": false\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "json",
            "optional": false,
            "field": "201",
            "description": "<p>message register confirmation message</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "201 Success-Response:",
          "content": "{\n   'msg': 'a confirmation message sent to user email'\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "json",
            "optional": false,
            "field": "406",
            "description": "<p>user already exists</p>"
          },
          {
            "group": "Error 4xx",
            "type": "json",
            "optional": false,
            "field": "401",
            "description": "<p>confirmation email did not send</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "406 Error-Response:",
          "content": "{\n   'error': 'this user already exists'\n}",
          "type": "json"
        },
        {
          "title": "401 Error-Response:",
          "content": "{\n   'error': 'problem with sending email'\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./app/api_v1/users.py",
    "groupTitle": "User"
  },
  {
    "type": "post",
    "url": "/change-password/:token",
    "title": "update user password",
    "name": "UpdatePassword",
    "group": "User",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "password",
            "description": "<p>new password</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n   \"password\": \"asdfgh\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "json",
            "optional": false,
            "field": "202",
            "description": "<p>change user password confirmation message</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "202 Success-Response:",
          "content": "{\n   'msg': 'user password changed successfully'\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "json",
            "optional": false,
            "field": "406",
            "description": "<p>user already exists</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "406 Error-Response:",
          "content": "{\n   'error': 'this user already exists'\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./app/api_v1/users.py",
    "groupTitle": "User"
  },
  {
    "type": "get",
    "url": "/delete_image/image_name",
    "title": "Delete image",
    "name": "delete_image",
    "group": "Utils",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "imageName",
            "description": "<p>name of image</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\"msg\": \"image deleted successfully\"}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "json",
            "optional": false,
            "field": "404",
            "description": "<p>the image not found</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "404 Error-Response:",
          "content": "{\n   \"error\": \"the image not found\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./app/api_v1/utils.py",
    "groupTitle": "Utils"
  },
  {
    "type": "post",
    "url": "/upload",
    "title": "Upload photo",
    "name": "upload_photo",
    "group": "Utils",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "File",
            "optional": false,
            "field": "imageFile",
            "description": "<p>Any image of .png, .jpg or .jpeg format</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "json",
            "optional": false,
            "field": "filename",
            "description": "<p>the name of file in server is returned</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\"filename\": \"10630a4e-0156-4734-8855-e01fd172173d.png\"}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "json",
            "optional": false,
            "field": "406",
            "description": "<p>the file format not supported</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "406 Error-Response:",
          "content": "{\n   \"error\": \"file type not supported\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./app/api_v1/utils.py",
    "groupTitle": "Utils"
  },
  {
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "optional": false,
            "field": "varname1",
            "description": "<p>No type.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "varname2",
            "description": "<p>With type.</p>"
          }
        ]
      }
    },
    "type": "",
    "url": "",
    "version": "0.0.0",
    "filename": "./doc/main.js",
    "group": "_home_farzin_seProject_presentation_maker_presenterHelper_doc_main_js",
    "groupTitle": "_home_farzin_seProject_presentation_maker_presenterHelper_doc_main_js",
    "name": ""
  }
] });
