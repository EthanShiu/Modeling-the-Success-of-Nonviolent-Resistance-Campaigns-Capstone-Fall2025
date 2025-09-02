# Setup///////////////////////////////////////////////////////////////////////////
library(shiny)
library(reticulate)
library(bslib)
library(shinythemes)
library(shinyjs)   
library(rsconnect)
library(reticulate)

# Used to deploy to Shinyapps.io

# Only install if packages are not already available
#required_packages <- c(
#  "pandas", "numpy", "shap", "matplotlib", "seaborn",
#  "scikit-learn", "scipy", "xlrd", "imbalanced-learn"
#)

# Check which are not yet available
#missing <- required_packages[!sapply(required_packages, py_module_available)]
#if (length(missing) > 0) {
#  message("Installing missing Python packages: ", paste(missing, collapse = ", "))
#  py_install(missing)
#} else {
#  message("All Python packages already available")
#}

# Now source your Python script
#source_python("ui_code.py")



custom_theme <- bs_theme(
  version = 5,
  bootswatch = "flatly",
  bg = "#FAF7F2",         # Background: light warm
  fg = "#333333",         # Foreground text
  primary = "#00274C",    # Navy for buttons, tabs
  secondary = "#C7A76C",  # Gold/tan for accents
  success = "#2A9D8F",    # Green for success
  info = "#6CA0DC",       # Soft blue info
  warning = "#F4A261",    # Muted orange warning
  danger = "#B22222",     # Dark red errors
  base_font = font_google("Roboto"),
  heading_font = font_google("Lora"),
  font_scale = 1.1
)

# ASSETS ////////////////////////////////////////////////////////////////////////
# Activate conda environment and source Python
use_condaenv("rf_project_env", required = TRUE)
message("Python config detected:")
print(py_config())

source_python("ui_code.py")

# Feature names
feature_names <- c(
  "div_class", "violent_flank", "log_rel_part", "camp_backlash", "total_part",
  "camp_duration", "wdrwl_support", "fatalities_range", "indiscrim",
  "sec_defect", "state_defect", "div_ethnicity", "sdirect", "ab_internat",
  "camp_support", "camp_structure", "camp_orgs", "media_outreach", "dom_media", "camp_goals"
)


dropdown_inputs <- list(
  "div_class" = c("No Class Diversity Within the Campaign" = 0, "Class Diversity Within the Campaign" = 1),
  "log_rel_part" = c(),
  "violent_flank" = c("Primarily Violent Campaign" = 0, "No Violent Flank" = 1, "Violent Flank" = 2),
  "camp_backlash" = c("No Observed Backlash" = 0, "Movement Surpressed" = 1, "Decreased Domestic Mobilization" = 2, "Increased Domestic Mobilization" = 3),
  "total_part" = c(),
  "camp_duration" = c(),
  "wdrwl_support" = c("Former State Supporters Maintain Support" = 0, "Former State Supporters Withdraw Support" = 1),
  "fatalities_range" = c("No Known Fatalities" = 0, "1-10 Fatalities" = 1, "11-25 Fatalities" = 2, "26-100 Fatalities" = 3, "101-1,000 Fatalities" = 4, "1,001-10,000 Fatalities" = 5, "10,001+ Fatalities" = 6),
  "indiscrim" = c("State Repression is Targeted" = 0, "State Repression is Indiscriminate" = 1),
  "sec_defect" = c("Security Forces / Military Defect from the Regime" = 1, "Security Forces / Military Remain Loyal to the Regime" = 0),
  "state_defect" = c("Civilian Buraucrats / Officials Defect from the Regime" = 1, "Civilian Bureaucrats / Officials Remain Loyal to the Regime" = 0),
  "div_ethnicity" = c("No Ethnic Diversity Within the Campaign" = 0, "Ethnic Diversity Within the Campaign" = 1),
  "sdirect" = c("International Sanctions Imposed" = 1, "No International Sanctions Imposed" = 0),
  "ab_internat" = c("No Observed International Backlash" = 0, "International Actors Condemn the State" = 1),
  "camp_support" = c("Campaign has Formal Overt Support From Other States" = 1, "Campaign has no Formal Overt Support from Other States" = 0),
  "camp_structure" = c("Consensus Based Participatory Campaign Structure" = 0, "Hierarchical Command and Control Campaign Structure" = 1),
  "camp_orgs" = c(),
  "media_outreach" = c("Campaign Spends Resources on an Information Campaign" = 1, "Campaign Does not Spend Resources on Public Relations" = 0),
  "dom_media" = c("No Traditional Domestic Media Covers the Campaign" = 0, "Moderate Coverage of the Campaign by Traditional Domestic Media" = 1, "High Coverage of the Campaign by Traditional Domestic Media" = 2),
  "camp_goals" = c("Regime Change" = 0, "Significant Institutional Reform" = 1, "Policy Change" = 2, "Territorial Secession" = 3, "Greater Autonomy" = 4, "Anti-Occupation" = 5)
)

named_features <- c(
  "Diversity of Class Within the Campaign" = "div_class",
  "Level of Violence Present in the Campaign " = "violent_flank",
  "Participation Relative to Country's Population" = "log_rel_part",
  "Campaign Response to Backlash" = "camp_backlash",
  "Total Participants" = "total_part",
  "Campaign Duration in Years" = "camp_duration",
  "Former State Supporters Withdraw Support" = "wdrwl_support",
  "Number of Fatalities" = "fatalities_range",
  "Is Repression Targeted or Indiscriminate" = "indiscrim",
  "Security Forces / Military Defections" = "sec_defect",
  "Civilian Officials / Bureaucrats Defections" = "state_defect",
  "Diversity of Ethnicity Within the Campaign" = "div_ethnicity",
  "International Sanctions Placed on the Regime" = "sdirect",
  "International Condemnation of the Regime" = "ab_internat",
  "Foreign Support for the Campaign" = "camp_support",
  "Campaign Structure" = "camp_structure",
  "New Organizations Affiliated with the Campaign" = "camp_orgs",
  "Campaign Invests in Media Outreach" = "media_outreach",
  "Traditional Domestic Media Covers the Campaign" = "dom_media",
  "Campaign Goals" = "camp_goals"
)

# UI buttons data 

df_ui_buttons_filtered <- read.csv("campaign_buttons_data.csv")

#Sri Lanka
row_sl <- df_ui_buttons_filtered[df_ui_buttons_filtered$id == 125, ]
sri_lanka_values <- as.list(row_sl[, !(names(row_sl) %in% c("id", "success"))])

# Algeria
row_al <- df_ui_buttons_filtered[df_ui_buttons_filtered$id == 6, ]
algeria_values <- as.list(row_al[, !(names(row_al) %in% c("id", "success"))])

# Tunisia
row_ts <- df_ui_buttons_filtered[df_ui_buttons_filtered$id == 311, ]
tunisia_values <- as.list(row_ts[, !(names(row_ts) %in% c("id", "success"))])

# Egypt
row_eg <- df_ui_buttons_filtered[df_ui_buttons_filtered$id == 331, ]
egypt_values <- as.list(row_eg[, !(names(row_eg) %in% c("id", "success"))])

# South Africa
row_sa <- df_ui_buttons_filtered[df_ui_buttons_filtered$id == 211, ]
safrica_values <- as.list(row_sa[, !(names(row_sa) %in% c("id", "success"))])

# Kosovo
row_ks <- df_ui_buttons_filtered[df_ui_buttons_filtered$id == 119, ]
kosovo_values <- as.list(row_ks[, !(names(row_ks) %in% c("id", "success"))])

# UI/////////////////////////////////////////////////////////////////////// 
ui <- fluidPage(
  theme = custom_theme,
  useShinyjs(),
  
  tags$head(
    tags$style(HTML("
      .well {
        background-color: #d6cfc2;
        border: none;
        box-shadow: none;
      }
    ")),
    tags$style(HTML("
      .sidebar {
        max-height: 90vh;
        overflow-y: auto;
        padding-right: 10px;
      }
    ")),
    tags$style(HTML("
      #prediction_output {
        font-size: 1.5em;
        color: #888888;
        border: 1px solid #cccccc;
        padding: 10px;
        border-radius: 5px;
        background-color: #f8f8f8;
        text-align: center;
        min-height: 50px;
      }
    "))
  ),
  
  div(style = "background-color: #2C3E50; padding: 10px; border-radius: 10px; margin-bottom: 5px;",
      h1("Resistance Campaign Success Predictor", style = "color: #ffffff; text-align: center;")
  ),
  
  tabsetPanel(  # ⬅️ Only ONE tabsetPanel that wraps everything
    tabPanel("Prediction",
             sidebarLayout(
               sidebarPanel(
                 div(class = "sidebar",
                     h4("Set Feature Values"),
                     lapply(feature_names, function(feat) {
                       choices <- dropdown_inputs[[feat]]
                       pretty_label <- names(named_features)[named_features == feat]
                       
                       if (!is.null(choices) && length(choices) > 0) {
                         selectInput(
                           inputId = feat, 
                           label = pretty_label, 
                           choices = choices, 
                           selectize = TRUE, 
                           width = "100%"
                         )
                       } else {
                         numericInput(
                           inputId = feat, 
                           label = pretty_label, 
                           value = 0, 
                           step = 0.1, 
                           width = "100%"
                         )
                       }
                     }),
                     br(),
                     actionButton("predict_btn", "Predict Success Probability", class = "btn-primary", style = "width: 100%; margin-top: 10px;")
                 )
               ),
               
               mainPanel(
                 div(
                   style = "background-color: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0px 0px 10px rgba(0,0,0,0.1); margin-top: 10px;",
                   fluidRow(
                     column(
                       width = 8,
                       h3("Predicted Probability of Success:")
                     ),
                     column(
                       width = 4,
                       div(
                         style = "text-align: right;",
                         actionButton(
                           inputId = "predict_btn_main",
                           label = "Predict Success Probability",
                           class = "btn-primary",
                           style = "width: 100%;"
                         )
                       )
                     )
                   ),
                   div(
                     style = "text-align: center; margin-top: 10px;",
                     verbatimTextOutput("prediction_output", placeholder = TRUE)
                   )
                ),
                 
                 div(
                   style = "background-color: #ffffff; padding: 15px; border-radius: 8px; box-shadow: 0px 0px 10px rgba(0,0,0,0.05); margin-top: 20px;",
                   h4("Explore Data from Historical Campaigns"),
                   fluidRow(
                     column(4, actionButton("prefill_tunisia", "Tunisia - Jasmine Revolution", style = "width: 100%; margin-bottom: 10px;")),
                     column(4, actionButton("prefill_egypt", "Egypt - Arab Spring 2011", style = "width: 100%; margin-bottom: 10px;")),
                     column(4, actionButton("prefill_south_africa", "South Africa - Anti-Apartheid", style = "width: 100%; margin-bottom: 10px;"))
                   ),
                   fluidRow(
                     column(4, actionButton("prefill_sri_lanka", "Sri Lanka - Tamil Tigers", style = "width: 100%; margin-bottom: 10px;")),
                     column(4, actionButton("prefill_algeria", "Algerian War - NLF", style = "width: 100%; margin-bottom: 10px;")),
                     column(4, actionButton("prefill_kosovo", "Kosovo - KLA Resistance", style = "width: 100%; margin-bottom: 10px;"))
                   )
                 )
               )
             )
    ),
    
    tabPanel(
      "SHAP Plots",
      sidebarLayout(
        sidebarPanel(
          h4("SHAP Dependence Plot Settings"),
          
          selectInput(
            "shap_feature",
            "Main Feature",
            choices = named_features,
            selected = "log_rel_part",
            selectize = TRUE
          ),
          
          selectInput(
            "interaction_feature",
            "Interaction Feature",
            choices = c("None", named_features),
            selected = "None",
            selectize = TRUE
          ),
          
          actionButton(
            "shap_plot_btn",
            "Generate SHAP Plot",
            class = "btn btn-warning",
            style = "width: 100%; margin-top: 10px;"
          ),
          
          hr(),
          
          h4("Feature Impact Summary (Beeswarm Plot)"),
          div(
            style = "background-color: #ffffff; padding: 10px; border-radius: 8px; box-shadow: 0px 0px 5px rgba(0,0,0,0.1);",
            img(src = "beeswarm_plot.png", style = "max-width: 100%; height: auto;")
          ),
          
          hr(),
          
          h4("Overall Feature Importance (Bar Chart)"),
          div(
            style = "background-color: #ffffff; padding: 10px; border-radius: 8px; box-shadow: 0px 0px 5px rgba(0,0,0,0.1);",
            img(src = "feature_importance_bar.png", style = "max-width: 100%; height: auto;")
          )
        ),
        
        mainPanel(
          h3("SHAP Dependence Plot"),
          
          h6(HTML("
        <b>Dependence Plot Explanation:</b>
        <ul>
          <li>Each dot represents a campaign.</li>
          <li>The x-axis shows the feature’s value (e.g., participation rate).</li>
          <li>The y-axis shows the SHAP value (impact on success prediction).</li>
          <li>Higher SHAP value = more likely success, lower = more likely failure.</li>
          <li>Color of the dots reveals the interactions with a different feature.</li>
        </ul>
      ")),
          
          imageOutput("shap_plot_output", height = "500px")
        )
      )
    )
  )
)

# Server////////////////////////////////////////////////////////////////////////////////
server <- function(input, output, session) {
  # Reactive input dictionary for Python
  user_input_dict <- reactive({
    setNames(lapply(feature_names, function(f) as.numeric(input[[f]])), feature_names)
  })
  
  # 1. Setup a reactive value for the prediction text
  prediction_text <- reactiveVal("Click 'Predict' to generate a score!")
  
  # 2. Render the prediction output
  output$prediction_output <- renderText({
    prediction_text()
  })
  
  # 3. Update the prediction text only when either Predict button is clicked
  observeEvent(c(input$predict_btn, input$predict_btn_main), {
    result <- predict_success_probability(user_input_dict())
    prediction_text(paste0(round(result * 100, 2), "%"))  # Now updates ONLY on click!
    
    runjs('
    var el = document.getElementById("prediction_output");
    el.style.color = "#000000";
    el.style.transition = "color 1s ease";
  ')
  }, ignoreNULL = TRUE, ignoreInit = TRUE)
  
    
  #Prefill Buttons
  
  # Sri-Lanka LTTE
  observeEvent(input$prefill_sri_lanka, {
    
    # Update each input
    lapply(names(sri_lanka_values), function(feat) {
      updateSelectInput(session, inputId = feat, selected = sri_lanka_values[[feat]])
      updateNumericInput(session, inputId = feat, value = sri_lanka_values[[feat]])
    })
    
    # Immediately run prediction after prefill
    result <- predict_success_probability(sri_lanka_values)
    prediction_text(paste0(round(result * 100, 2), "%"))
    
    # After clicking, change the color of the prediction box
    runjs('
      var el = document.getElementById("prediction_output");
      el.style.color = "#000000";
      el.style.transition = "color 1s ease";  // smooth fade transition
    ')
  }, ignoreNULL = TRUE, ignoreInit = TRUE)
  
  # Algerian Revolt NLF
  observeEvent(input$prefill_algeria, {
    
    # Update each input
    lapply(names(algeria_values), function(feat) {
      updateSelectInput(session, inputId = feat, selected = algeria_values[[feat]])
      updateNumericInput(session, inputId = feat, value = algeria_values[[feat]])
    })
    
    # Immediately run prediction after prefill
    result <- predict_success_probability(algeria_values)
    prediction_text(paste0(round(result * 100, 2), "%"))
    
    # After clicking, change the color of the prediction box
    runjs('
      var el = document.getElementById("prediction_output");
      el.style.color = "#000000";
      el.style.transition = "color 1s ease";  // smooth fade transition
    ')
  }, ignoreNULL = TRUE, ignoreInit = TRUE)
  
  # Jasmine Revolution
  observeEvent(input$prefill_tunisia, {
    
    # Update each input
    lapply(names(tunisia_values), function(feat) {
      updateSelectInput(session, inputId = feat, selected = tunisia_values[[feat]])
      updateNumericInput(session, inputId = feat, value = tunisia_values[[feat]])
    })
    
    # Immediately run prediction after prefill
    result <- predict_success_probability(tunisia_values)
    prediction_text(paste0(round(result * 100, 2), "%"))
    
    # After clicking, change the color of the prediction box
    runjs('
      var el = document.getElementById("prediction_output");
      el.style.color = "#000000";
      el.style.transition = "color 1s ease";  // smooth fade transition
    ')
  }, ignoreNULL = TRUE, ignoreInit = TRUE)
  
  # Egyptian Arab Spring
  observeEvent(input$prefill_egypt, {
    
    # Update each input
    lapply(names(egypt_values), function(feat) {
      updateSelectInput(session, inputId = feat, selected = egypt_values[[feat]])
      updateNumericInput(session, inputId = feat, value = egypt_values[[feat]])
    })
    
    # Immediately run prediction after prefill
    result <- predict_success_probability(egypt_values)
    prediction_text(paste0(round(result * 100, 2), "%"))
    
    # After clicking, change the color of the prediction box
    runjs('
      var el = document.getElementById("prediction_output");
      el.style.color = "#000000";
      el.style.transition = "color 1s ease";  // smooth fade transition
    ')
  }, ignoreNULL = TRUE, ignoreInit = TRUE)
  
  # South Africa
  observeEvent(input$prefill_south_africa, {
    
    # Update each input
    lapply(names(safrica_values), function(feat) {
      updateSelectInput(session, inputId = feat, selected = safrica_values[[feat]])
      updateNumericInput(session, inputId = feat, value = safrica_values[[feat]])
    })
    
    # Immediately run prediction after prefill
    result <- predict_success_probability(safrica_values)
    prediction_text(paste0(round(result * 100, 2), "%"))
    
    # After clicking, change the color of the prediction box
    runjs('
      var el = document.getElementById("prediction_output");
      el.style.color = "#000000";
      el.style.transition = "color 1s ease";  // smooth fade transition
    ')
  }, ignoreNULL = TRUE, ignoreInit = TRUE)
  
  # Kosovo KLA
  observeEvent(input$prefill_kosovo, {
    
    # Update each input
    lapply(names(kosovo_values), function(feat) {
      updateSelectInput(session, inputId = feat, selected = kosovo_values[[feat]])
      updateNumericInput(session, inputId = feat, value = kosovo_values[[feat]])
    })
    
    # Immediately run prediction after prefill
    result <- predict_success_probability(kosovo_values)
    prediction_text(paste0(round(result * 100, 2), "%"))
    
    # After clicking, change the color of the prediction box
    runjs('
      var el = document.getElementById("prediction_output");
      el.style.color = "#000000";
      el.style.transition = "color 1s ease";  // smooth fade transition
    ')
  }, ignoreNULL = TRUE, ignoreInit = TRUE)
  
  # SHAP plot auto generate
  observe({
    output$shap_plot_output <- renderImage({
      tryCatch({
        message("Generating plot for: log_rel_part / div_class")
        
        
        fig_path <- shap_dependence_plot(
          main_feature = "log_rel_part",
          interaction_feature = "div_class",
          shap_values = shap_values,
          X = X
        )
        
        if (!is.null(fig_path) && file.exists(fig_path)) {
          list(
            src = fig_path,
            contentType = "image/png",
            alt = "SHAP Dependence Plot"
          )
        } else {
          list(src = NULL, alt = "No plot returned.")
        }
      }, error = function(e) {
        message("SHAP plot error:", e$message)
        list(src = NULL, alt = "Error generating plot.")
      })
    }, deleteFile = TRUE)
  })
  
  # SHAP Plot button
  observeEvent(input$shap_plot_btn, {
    output$shap_plot_output <- renderImage({
      tryCatch({
        message("Generating plot for: ", input$shap_feature, "/", input$interaction_feature)
        
        interaction_feature_clean <- if (input$interaction_feature == "None") {
          NULL
        } else {
          input$interaction_feature
        }
        
        
        fig_path <- shap_dependence_plot(
          main_feature = input$shap_feature,
          interaction_feature = interaction_feature_clean,
          shap_values = shap_values,
          X = X
        )
        
        if (!is.null(fig_path) && file.exists(fig_path)) {
          list(
            src = fig_path,
            contentType = "image/png",
            alt = "SHAP Dependence Plot"
          )
        } else {
          list(src = NULL, alt = "No plot returned.")
        }
      }, error = function(e) {
        message("SHAP plot error:", e$message)
        list(src = NULL, alt = "Error generating plot.")
      })
    }, deleteFile = TRUE)
  })
  
}

shinyApp(ui = ui, server = server)
