#!/usr/bin/python

from datadog import initialize, api

options = {
    'api_key': '',
    'app_key': ''
}

initialize(**options)

title = 'AWS Workspaces Integration WIP'
widgets = [{
      "definition": {
        "autoscale": True,
        "precision": 2,
        "requests": [
          {
            "aggregator": "avg",
            "conditional_formats": [],
            "q": "avg:aws.workspaces.stopped{$Directory,$Region}"
          }
        ],
        "time": {},
        "title": "Workspaces Stopped",
        "title_align": "left",
        "title_size": "16",
        "type": "query_value"
      },
      "layout": {
        "height": 12,
        "width": 15,
        "x": 17,
        "y": 38
      }
    },
    {
      "definition": {
        "autoscale": True,
        "precision": 2,
        "requests": [
          {
            "aggregator": "avg",
            "conditional_formats": [],
            "q": "avg:aws.workspaces.available{$Directory,$Region}"
          }
        ],
        "time": {},
        "title": "Workspaces Available",
        "title_align": "left",
        "title_size": "16",
        "type": "query_value"
      },
      "layout": {
        "height": 12,
        "width": 15,
        "x": 1,
        "y": 38
      }
    },
    {
      "definition": {
        "sizing": "center",
        "type": "image",
        "url": "https://docs.secureauth.com/download/attachments/45384505/Amazon-WorkSpaces-1.png"
      },
      "layout": {
        "height": 26,
        "width": 28,
        "x": 1,
        "y": 2
      }
    },
    {
      "definition": {
        "autoscale": True,
        "precision": 2,
        "requests": [
          {
            "aggregator": "avg",
            "conditional_formats": [],
            "q": "avg:aws.workspaces.maintenance{$Directory,$Region}"
          }
        ],
        "time": {},
        "title": "Workspaces in Maintainence",
        "title_align": "left",
        "title_size": "16",
        "type": "query_value"
      },
      "layout": {
        "height": 12,
        "width": 15,
        "x": 17,
        "y": 52
      }
    },
    {
      "definition": {
        "autoscale": True,
        "precision": 2,
        "requests": [
          {
            "aggregator": "avg",
            "conditional_formats": [],
            "q": "avg:aws.workspaces.unhealthy{$Directory,$Region}"
          }
        ],
        "time": {},
        "title": "Workspaces Unhealthy",
        "title_align": "left",
        "title_size": "16",
        "type": "query_value"
      },
      "layout": {
        "height": 12,
        "width": 15,
        "x": 1,
        "y": 52
      }
    },
    {
      "definition": {
        "background_color": "gray",
        "content": "Workspaces Status",
        "font_size": "24",
        "show_tick": False,
        "text_align": "center",
        "tick_edge": "bottom",
        "tick_pos": "50%",
        "type": "note"
      },
      "layout": {
        "height": 5,
        "width": 31,
        "x": 1,
        "y": 30
      }
    },
    {
      "definition": {
        "requests": [
          {
            "conditional_formats": [],
            "q": "top(avg:aws.workspaces.user_connected{*} by {region}, 10, 'mean', 'desc')",
            "style": {
              "palette": "dog_classic"
            }
          }
        ],
        "time": {},
        "title": "Users Connected By Region",
        "title_align": "left",
        "title_size": "16",
        "type": "toplist"
      },
      "layout": {
        "height": 33,
        "width": 41,
        "x": 1,
        "y": 74
      }
    },
    {
      "definition": {
        "legend_size": "0",
        "requests": [
          {
            "display_type": "bars",
            "q": "avg:aws.workspaces.connection_attempt{$Directory,$Region,$WorkspaceInstance}.as_count()",
            "style": {
              "line_type": "solid",
              "line_width": "normal",
              "palette": "dog_classic"
            }
          }
        ],
        "show_legend": False,
        "time": {},
        "title": "Connections Attempted",
        "title_align": "left",
        "title_size": "16",
        "type": "timeseries"
      },
      "layout": {
        "height": 15,
        "width": 56,
        "x": 47,
        "y": 10
      }
    },
    {
      "definition": {
        "background_color": "gray",
        "content": "Connection Information",
        "font_size": "24",
        "show_tick": False,
        "text_align": "center",
        "tick_edge": "bottom",
        "tick_pos": "50%",
        "type": "note"
      },
      "layout": {
        "height": 5,
        "width": 31,
        "x": 56,
        "y": 3
      }
    },
    {
      "definition": {
        "legend_size": "0",
        "requests": [
          {
            "display_type": "bars",
            "q": "avg:aws.workspaces.connection_failure{$Directory,$Region,$WorkspaceInstance}.as_count()",
            "style": {
              "line_type": "solid",
              "line_width": "normal",
              "palette": "dog_classic"
            }
          }
        ],
        "show_legend": False,
        "time": {},
        "title": "Connection Failures",
        "title_align": "left",
        "title_size": "16",
        "type": "timeseries"
      },
      "layout": {
        "height": 15,
        "width": 56,
        "x": 47,
        "y": 44
      }
    },
    {
      "definition": {
        "legend_size": "0",
        "requests": [
          {
            "display_type": "bars",
            "q": "avg:aws.workspaces.connection_success{$Directory,$Region,$WorkspaceInstance}.as_count()",
            "style": {
              "line_type": "solid",
              "line_width": "normal",
              "palette": "dog_classic"
            }
          }
        ],
        "show_legend": False,
        "time": {},
        "title": "Connection Successes",
        "title_align": "left",
        "title_size": "16",
        "type": "timeseries"
      },
      "layout": {
        "height": 15,
        "width": 56,
        "x": 47,
        "y": 27
      }
    },
    {
      "definition": {
        "legend_size": "0",
        "requests": [
          {
            "display_type": "bars",
            "q": "avg:aws.workspaces.in_session_latency{$Directory,$Region,$WorkspaceInstance}",
            "style": {
              "line_type": "solid",
              "line_width": "normal",
              "palette": "dog_classic"
            }
          }
        ],
        "show_legend": False,
        "time": {},
        "title": "Connection Latency",
        "title_align": "left",
        "title_size": "16",
        "type": "timeseries"
      },
      "layout": {
        "height": 15,
        "width": 56,
        "x": 47,
        "y": 61
      }
    },
    {
      "definition": {
        "background_color": "gray",
        "content": "Users over Region",
        "font_size": "24",
        "show_tick": False,
        "text_align": "center",
        "tick_edge": "bottom",
        "tick_pos": "50%",
        "type": "note"
      },
      "layout": {
        "height": 5,
        "width": 31,
        "x": 6,
        "y": 68
      }
    }]
layout_type = 'free'
description = 'Dashboard For AWS Workspaces Integraiton'
is_read_only = True
notify_list = ['ryan.hennessy@datatdoghq.com']
template_variables = [{
      "default": "*",
      "name": "Directory",
      "prefix": "directoryid"
    },
    {
      "default": "*",
      "name": "Region",
      "prefix": "region"
    },
    {
      "default": "*",
      "name": "WorkspaceInstance",
      "prefix": "workspaceid"
    }]


api.Dashboard.create(title=title,
                     widgets=widgets,
                     layout_type=layout_type,
                     description=description,
                     is_read_only=is_read_only,
                     notify_list=notify_list,
                     template_variables=template_variables)

