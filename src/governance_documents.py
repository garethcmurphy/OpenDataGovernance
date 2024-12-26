#!/usr/bin/env python3
"""A class to generate markdown content for governance documents."""
import os

class GovernanceDocuments:
    """A class to generate markdown content for governance documents."""
    def __init__(self, base_folder="Data_Governance_Documents"):
        self.base_folder = base_folder
        self.documents = [
            (
                "Code_of_Conduct",
                """This document sets ethical standards and expectations 
                for behavior across the organization.""",
            ),
            (
                "Research_Ethics_Policy",
                """This document outlines ethical principles for conducting research, 
                including consent and humane animal use.""",
            ),
            (
                "Data_Integrity_Policy",
                """This document establishes rules for ensuring the accuracy, 
                completeness, and consistency of R&D data.""",
            ),
            (
                "Collaboration_Guidelines",
                """This document provides rules for working with external partners, 
                including confidentiality and IP considerations.""",
            ),
            (
                "AI_ML_Governance_Framework",
                """This document details responsible AI use in research, 
                addressing data privacy, bias, and explainability.""",
            ),
            (
                "Study_Design_Execution_SOP",
                """This document provides guidelines for planning and running experiments, 
                such as assay development and cell culture.""",
            ),
            (
                "Data_Collection_Documentation_SOP",
                """This document defines procedures for capturing experimental data 
                in compliance with Good Laboratory Practices (GLP).""",
            ),
            (
                "Biosafety_SOP",
                """This document addresses handling of hazardous materials, 
                pathogens, and genetically modified organisms.""",
            ),
            (
                "Sample_Management_SOP",
                """This document covers the tracking, storage, and disposal 
                of biological and chemical samples.""",
            ),
            (
                "Data_Sharing_Reporting_SOP",
                """This document describes how to share results internally and externally 
                while ensuring FAIR principles.""",
            ),
            (
                "Scientific_Governance_Framework",
                """This document defines the roles, responsibilities, and processes 
                for scientific decision-making and oversight.""",
            ),
            (
                "Data_Governance_Framework",
                """This document establishes rules for managing and sharing data, 
                including metadata standards, ontologies, and secure storage.""",
            ),
            (
                "Portfolio_Governance_Guidelines",
                """This document provides a framework for evaluating 
                and prioritizing R&D projects.""",
            ),
            (
                "Risk_Management_Plan",
                """This document identifies potential risks in early R&D 
                and mitigation strategies.""",
            ),
            (
                "Material_Transfer_Agreement",
                """This document regulates the transfer of materials 
                between organizations.""",
            ),
            (
                "Intellectual_Property_Management",
                """This document outlines how discoveries are patented 
                and protected.""",
            ),
            (
                "Clinical_Trial_Transition_Framework",
                """This document defines requirements for moving projects 
                into clinical phases.""",
            ),
            (
                "R&D_Roadmap",
                """This document lays out the strategic vision 
                and milestones for early research programs.""",
            ),
            (
                "Capability_Development_Plan",
                """This document details how to build and maintain expertise, 
                technologies, and tools.""",
            ),
            (
                "Innovation_Governance_Strategy",
                """This document guides how innovation is managed 
                and integrated into R&D processes.""",
            ),
            (
                "Joint_Research_Agreement",
                """This document details terms for shared R&D projects.""",
            ),
            (
                "Confidentiality_Agreement",
                """This document protects sensitive information 
                shared with external partners.""",
            ),
            (
                "License_Agreement",
                """This document manages access to proprietary technology 
                or compounds.""",
            ),
            (
                "Data_Management_Plan",
                """This document specifies how research data will be collected, 
                stored, and shared.""",
            ),
            (
                "FAIR_Data_Guidelines",
                """This document ensures research data is Findable, 
                Accessible, Interoperable, and Reusable.""",
            ),
            (
                "Ontology_Development_Guidelines",
                """This document provides rules for aligning datasets 
                with standardized vocabularies.""",
            ),
            (
                "Training_Documentation",
                """This document tracks compliance with mandatory training 
                (e.g., GLP, biosafety, or data integrity).""",
            ),
        ]

    def generate_markdown_files(self):
        """Generate markdown files for governance documents."""
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

        for title, description in self.documents:
            filename = f"{title}.md"
            filepath = os.path.join(self.base_folder, filename)
            with open(filepath, 'w', encoding="ascii") as file:
                file.write(f"# {title.replace('_', ' ')}\n\n{description}\n")

# Example usage
if __name__ == "__main__":
    gov_docs = GovernanceDocuments()
    gov_docs.generate_markdown_files()
