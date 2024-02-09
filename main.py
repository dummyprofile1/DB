from Database import *
import streamlit as st
import time
from streamlit_option_menu import option_menu

def main():
    st.title("Art School App")
    create_database()


    selected = option_menu(
        menu_title=None,
        options=["Add Student", "Search for Student","Filter","Delete Student with Student id","Update Student info based on Student ID", "View Database"],
        orientation="horizontal",
    )
    if selected == "Add Student":
        studentid = st.text_input("StudentID")
        fname = st.text_input("FirstName")
        lname = st.text_input("LastName")
        ArtSchool = st.selectbox(label="ArtSchool", options=['1', '2'])
        if ArtSchool == '1':
            Course = st.selectbox(label="Course", options=['MA', 'MA+PhD', 'PhD'])
        else:
            Course = st.selectbox(label="Course", options=['MFA', 'PhD'])

        # Program = st.text_input("Program")
        if Course == 'MA' or Course == 'MA+PhD':
            Program = st.selectbox(label="Program",
                                   options=['LIT', 'HUMA', 'VPAS', 'HIST', 'HI', 'LATS', 'AHST', 'ATEC'])
        elif Course == 'Phd':
            Program = st.selectbox(label="Program",
                                   options=['LIT', 'HUMA', 'VPAS', 'HIST', 'HI', 'LATS', 'AHST', 'ATEC',
                                            'Creative practice', 'Animation', 'Game design'])
        else:
            Program = st.selectbox(label="Program", options=['Creative practice', 'Animation', 'Game design'])
        SubPlanText = st.text_input("SubPlanText")
        FirstSemester = st.text_input("FirstSemester")
        Catalog = st.text_input("Catalog")
        HGHRcertCatalog = st.text_input("HGHRcertCatalog")
        TranslCertCatalog = st.text_input("TranslCertCatalog")
        CRWcertCatalog = st.text_input("CRWcertCatalog")
        FacultyAdvisor = st.text_input("FacultyAdvisor")
        TAYN = st.text_input("TAYN")
        LatestMilestoneFormSem = st.text_input("LatestMilestoneFormSem")
        InternationalStudentYN = st.selectbox(label="InternationalStudentYN", options=['Yes', 'No'])
        Language = st.text_input("Language")
        LanguageDateFulfilled = st.text_input("LanguageDateFulfilled")
        LanguageReqWaivedBy = st.text_input("LanguageReqWaivedBy")
        LanguageReqWaivedDate = st.text_input("LanguageReqWaivedDate")
        ExamCommitteeFormDate = st.text_input("ExamCommitteeFormDate")
        ExamCommChair = st.text_input("ExamCommChair")
        ExamCommCoChair = st.text_input("ExamCommCoChair")
        ExamComm2nd = st.text_input("ExamComm2nd")
        ExamComm3rd = st.text_input("ExamComm3rd")
        FirstSemRegFEP = st.text_input("FirstSemRegFEP")
        ExamsCompleteDate = st.text_input("ExamsCompleteDate")
        ExamResult = st.text_input("ExamResult")
        RegDissPropSem = st.text_input("RegDissPropSem")
        ProposalApprovedDate = st.text_input("ProposalApprovedDate")
        DissertationTitle = st.text_input("DissertationTitle")
        CommitteeFormOnFileYN = st.text_input("CommitteeFormOnFileYN")
        DissCommChair = st.text_input("DissCommChair")
        DissCommCoChair = st.text_input("DissCommCoChair")
        DissComm2nd = st.text_input("DissComm2nd")
        DissComm3rd = st.text_input("DissComm3rd")
        DissComm4th = st.text_input("DissComm4th")
        AdditionalDissComm = st.text_input("AdditionalDissComm")
        GraduatedSemester = st.text_input("GraduatedSemester")
        Inactive = st.text_input("Inactive")
        Notes = st.text_input("Notes")
        MAProfessionalResearch = st.text_input("MAProfessionalResearch")
        LanguageSeePhD = st.text_input("LanguageSeePhD")
        PortfolioProposalApprovedDate = st.text_input("PortfolioProposalApprovedDate")
        CommitteeChair = st.text_input("CommitteeChair")
        CoChair = st.text_input("CoChair")
        Comm2 = st.text_input("Comm2")
        Comm3 = st.text_input("Comm3")
        DefenseDate = st.text_input("DefenseDate")
        Result = st.text_input("Result")
        GraduatedSem = st.text_input("GraduatedSem")
        InactiveCheck = st.text_input("InactiveCheck")
        PersonalEmail = st.text_input("PersonalEmail")
        Address = st.text_input("Address")
        Country = st.text_input("Country")
        Employment = st.text_input("Employment")
        SocialMedia = st.text_input("SocialMedia")
        AlumniNotes = st.text_input("AlumniNotes")
        if st.button("Add"):
            add_student(lname, fname, studentid, Course, Program, ArtSchool, SubPlanText, FirstSemester, Catalog,HGHRcertCatalog, TranslCertCatalog, \
                        CRWcertCatalog, FacultyAdvisor, TAYN, LatestMilestoneFormSem, InternationalStudentYN \
                        , Language, LanguageDateFulfilled, LanguageReqWaivedBy, LanguageReqWaivedDate,ExamCommitteeFormDate, \
                        ExamCommChair, ExamCommCoChair, ExamComm2nd, ExamComm3rd, FirstSemRegFEP, ExamsCompleteDate, \
                        ExamResult, RegDissPropSem, ProposalApprovedDate, DissertationTitle, CommitteeFormOnFileYN, \
                        DissCommChair, DissCommCoChair, DissComm2nd, DissComm3rd, DissComm4th, AdditionalDissComm,GraduatedSemester, \
                        Inactive, Notes, MAProfessionalResearch, LanguageSeePhD, PortfolioProposalApprovedDate,CommitteeChair, \
                        CoChair, Comm2, Comm3, DefenseDate, Result, GraduatedSem, InactiveCheck, PersonalEmail, Address,Country, \
                        Employment, SocialMedia, AlumniNotes)
            st.session_state
            success = st.warning("Student added Successfully")
            time.sleep(2)
            success.empty()

    if selected == "Search for Student":
        studentid = st.text_input("StudentID")
        fname = st.text_input("FirstName")
        lname = st.text_input("LastName")
        ArtSchool = st.selectbox(label="ArtSchool", options=['1', '2'])
        if ArtSchool == '1':
            Course = st.selectbox(label="Course", options=['MA', 'MA+PhD', 'PhD'])
        else:
            Course = st.selectbox(label="Course", options=['MFA', 'PhD'])

        # Program = st.text_input("Program")
        if Course == 'MA' or Course == 'MA+PhD':
            Program = st.selectbox(label="Program",
                                   options=['LIT', 'HUMA', 'VPAS', 'HIST', 'HI', 'LATS', 'AHST', 'ATEC'])
        elif Course == 'Phd':
            Program = st.selectbox(label="Program",
                                   options=['LIT', 'HUMA', 'VPAS', 'HIST', 'HI', 'LATS', 'AHST', 'ATEC',
                                            'Creative practice', 'Animation', 'Game design'])
        else:
            Program = st.selectbox(label="Program", options=['Creative practice', 'Animation', 'Game design'])
        SubPlanText = st.text_input("SubPlanText")
        FirstSemester = st.text_input("FirstSemester")
        Catalog = st.text_input("Catalog")
        HGHRcertCatalog = st.text_input("HGHRcertCatalog")
        TranslCertCatalog = st.text_input("TranslCertCatalog")
        CRWcertCatalog = st.text_input("CRWcertCatalog")
        FacultyAdvisor = st.text_input("FacultyAdvisor")
        TAYN = st.text_input("TAYN")
        LatestMilestoneFormSem = st.text_input("LatestMilestoneFormSem")
        InternationalStudentYN = st.selectbox(label="InternationalStudentYN", options=['Yes', 'No'])
        Language = st.text_input("Language")
        LanguageDateFulfilled = st.text_input("LanguageDateFulfilled")
        LanguageReqWaivedBy = st.text_input("LanguageReqWaivedBy")
        LanguageReqWaivedDate = st.text_input("LanguageReqWaivedDate")
        ExamCommitteeFormDate = st.text_input("ExamCommitteeFormDate")
        ExamCommChair = st.text_input("ExamCommChair")
        ExamCommCoChair = st.text_input("ExamCommCoChair")
        ExamComm2nd = st.text_input("ExamComm2nd")
        ExamComm3rd = st.text_input("ExamComm3rd")
        FirstSemRegFEP = st.text_input("FirstSemRegFEP")
        ExamsCompleteDate = st.text_input("ExamsCompleteDate")
        ExamResult = st.text_input("ExamResult")
        RegDissPropSem = st.text_input("RegDissPropSem")
        ProposalApprovedDate = st.text_input("ProposalApprovedDate")
        DissertationTitle = st.text_input("DissertationTitle")
        CommitteeFormOnFileYN = st.text_input("CommitteeFormOnFileYN")
        DissCommChair = st.text_input("DissCommChair")
        DissCommCoChair = st.text_input("DissCommCoChair")
        DissComm2nd = st.text_input("DissComm2nd")
        DissComm3rd = st.text_input("DissComm3rd")
        DissComm4th = st.text_input("DissComm4th")
        AdditionalDissComm = st.text_input("AdditionalDissComm")
        GraduatedSemester = st.text_input("GraduatedSemester")
        Inactive = st.text_input("Inactive")
        Notes = st.text_input("Notes")
        MAProfessionalResearch = st.text_input("MAProfessionalResearch")
        LanguageSeePhD = st.text_input("LanguageSeePhD")
        PortfolioProposalApprovedDate = st.text_input("PortfolioProposalApprovedDate")
        CommitteeChair = st.text_input("CommitteeChair")
        CoChair = st.text_input("CoChair")
        Comm2 = st.text_input("Comm2")
        Comm3 = st.text_input("Comm3")
        DefenseDate = st.text_input("DefenseDate")
        Result = st.text_input("Result")
        GraduatedSem = st.text_input("GraduatedSem")
        InactiveCheck = st.text_input("InactiveCheck")
        PersonalEmail = st.text_input("PersonalEmail")
        Address = st.text_input("Address")
        Country = st.text_input("Country")
        Employment = st.text_input("Employment")
        SocialMedia = st.text_input("SocialMedia")
        AlumniNotes = st.text_input("AlumniNotes")
        if st.button("Search"):
            message = st.warning("Here is the search result")
            students = search_student(lname, fname, studentid, Course, Program, ArtSchool, SubPlanText, FirstSemester, Catalog,HGHRcertCatalog, TranslCertCatalog, \
                            CRWcertCatalog, FacultyAdvisor, TAYN, LatestMilestoneFormSem, InternationalStudentYN \
                            , Language, LanguageDateFulfilled, LanguageReqWaivedBy, LanguageReqWaivedDate,ExamCommitteeFormDate, \
                            ExamCommChair, ExamCommCoChair, ExamComm2nd, ExamComm3rd, FirstSemRegFEP, ExamsCompleteDate, \
                            ExamResult, RegDissPropSem, ProposalApprovedDate, DissertationTitle, CommitteeFormOnFileYN, \
                            DissCommChair, DissCommCoChair, DissComm2nd, DissComm3rd, DissComm4th, AdditionalDissComm,GraduatedSemester, \
                            Inactive, Notes, MAProfessionalResearch, LanguageSeePhD, PortfolioProposalApprovedDate,CommitteeChair, \
                            CoChair, Comm2, Comm3, DefenseDate, Result, GraduatedSem, InactiveCheck, PersonalEmail, Address,Country, \
                            Employment, SocialMedia, AlumniNotes)
            st.table(students)

            time.sleep(2)
            message.empty()
    if selected == "Delete Student with Student id" :
        studentid = st.text_input("StudentID")
        if st.button("Delete"):
            delete_student(studentid)
            message = st.warning("Deleted")
            time.sleep(2)
            message.empty()
    if selected == "Update Student info based on Student ID":
        studentid = st.text_input("StudentID")
        fname = st.text_input("FirstName")
        lname = st.text_input("LastName")
        ArtSchool = st.selectbox(label="ArtSchool", options=['1', '2'])
        if ArtSchool == '1':
            Course = st.selectbox(label="Course", options=['MA', 'MA+PhD', 'PhD'])
        else:
            Course = st.selectbox(label="Course", options=['MFA', 'PhD'])

        # Program = st.text_input("Program")
        if Course == 'MA' or Course == 'MA+PhD':
            Program = st.selectbox(label="Program",
                                   options=['LIT', 'HUMA', 'VPAS', 'HIST', 'HI', 'LATS', 'AHST', 'ATEC'])
        elif Course == 'Phd':
            Program = st.selectbox(label="Program",
                                   options=['LIT', 'HUMA', 'VPAS', 'HIST', 'HI', 'LATS', 'AHST', 'ATEC',
                                            'Creative practice', 'Animation', 'Game design'])
        else:
            Program = st.selectbox(label="Program", options=['Creative practice', 'Animation', 'Game design'])
        SubPlanText = st.text_input("SubPlanText")
        FirstSemester = st.text_input("FirstSemester")
        Catalog = st.text_input("Catalog")
        HGHRcertCatalog = st.text_input("HGHRcertCatalog")
        TranslCertCatalog = st.text_input("TranslCertCatalog")
        CRWcertCatalog = st.text_input("CRWcertCatalog")
        FacultyAdvisor = st.text_input("FacultyAdvisor")
        TAYN = st.text_input("TAYN")
        LatestMilestoneFormSem = st.text_input("LatestMilestoneFormSem")
        InternationalStudentYN = st.selectbox(label="InternationalStudentYN", options=['Yes', 'No'])
        Language = st.text_input("Language")
        LanguageDateFulfilled = st.text_input("LanguageDateFulfilled")
        LanguageReqWaivedBy = st.text_input("LanguageReqWaivedBy")
        LanguageReqWaivedDate = st.text_input("LanguageReqWaivedDate")
        ExamCommitteeFormDate = st.text_input("ExamCommitteeFormDate")
        ExamCommChair = st.text_input("ExamCommChair")
        ExamCommCoChair = st.text_input("ExamCommCoChair")
        ExamComm2nd = st.text_input("ExamComm2nd")
        ExamComm3rd = st.text_input("ExamComm3rd")
        FirstSemRegFEP = st.text_input("FirstSemRegFEP")
        ExamsCompleteDate = st.text_input("ExamsCompleteDate")
        ExamResult = st.text_input("ExamResult")
        RegDissPropSem = st.text_input("RegDissPropSem")
        ProposalApprovedDate = st.text_input("ProposalApprovedDate")
        DissertationTitle = st.text_input("DissertationTitle")
        CommitteeFormOnFileYN = st.text_input("CommitteeFormOnFileYN")
        DissCommChair = st.text_input("DissCommChair")
        DissCommCoChair = st.text_input("DissCommCoChair")
        DissComm2nd = st.text_input("DissComm2nd")
        DissComm3rd = st.text_input("DissComm3rd")
        DissComm4th = st.text_input("DissComm4th")
        AdditionalDissComm = st.text_input("AdditionalDissComm")
        GraduatedSemester = st.text_input("GraduatedSemester")
        Inactive = st.text_input("Inactive")
        Notes = st.text_input("Notes")
        MAProfessionalResearch = st.text_input("MAProfessionalResearch")
        LanguageSeePhD = st.text_input("LanguageSeePhD")
        PortfolioProposalApprovedDate = st.text_input("PortfolioProposalApprovedDate")
        CommitteeChair = st.text_input("CommitteeChair")
        CoChair = st.text_input("CoChair")
        Comm2 = st.text_input("Comm2")
        Comm3 = st.text_input("Comm3")
        DefenseDate = st.text_input("DefenseDate")
        Result = st.text_input("Result")
        GraduatedSem = st.text_input("GraduatedSem")
        InactiveCheck = st.text_input("InactiveCheck")
        PersonalEmail = st.text_input("PersonalEmail")
        Address = st.text_input("Address")
        Country = st.text_input("Country")
        Employment = st.text_input("Employment")
        SocialMedia = st.text_input("SocialMedia")
        AlumniNotes = st.text_input("AlumniNotes")
        if st.button("Update"):
            update_student(studentid, fname, lname, Course, Program, ArtSchool, SubPlanText, FirstSemester, Catalog,
                            HGHRcertCatalog, TranslCertCatalog, \
                            CRWcertCatalog, FacultyAdvisor, TAYN, LatestMilestoneFormSem, InternationalStudentYN \
                            , Language, LanguageDateFulfilled, LanguageReqWaivedBy, LanguageReqWaivedDate,
                            ExamCommitteeFormDate, \
                            ExamCommChair, ExamCommCoChair, ExamComm2nd, ExamComm3rd, FirstSemRegFEP, ExamsCompleteDate, \
                            ExamResult, RegDissPropSem, ProposalApprovedDate, DissertationTitle, CommitteeFormOnFileYN, \
                            DissCommChair, DissCommCoChair, DissComm2nd, DissComm3rd, DissComm4th, AdditionalDissComm,
                            GraduatedSemester, \
                            Inactive, Notes, MAProfessionalResearch, LanguageSeePhD, PortfolioProposalApprovedDate,
                            CommitteeChair, \
                            CoChair, Comm2, Comm3, DefenseDate, Result, GraduatedSem, InactiveCheck, PersonalEmail, Address,
                            Country, \
                            Employment, SocialMedia, AlumniNotes
                            )
            message = st.warning("Updated")
            time.sleep(2)
            message.empty()

    if selected == "Filter":
        studentid = None
        fname = st.text_input("FirstName")
        lname = st.text_input("LastName")
        ArtSchool = st.text_input("ArtSchool")

        Course = st.text_input("Course")


        # Program = st.text_input("Program")
        Program = st.text_input("Program")

        SubPlanText = st.text_input("SubPlanText")
        FirstSemester = st.text_input("FirstSemester")
        Catalog = st.text_input("Catalog")
        HGHRcertCatalog = st.text_input("HGHRcertCatalog")
        TranslCertCatalog = st.text_input("TranslCertCatalog")
        CRWcertCatalog = st.text_input("CRWcertCatalog")
        FacultyAdvisor = st.text_input("FacultyAdvisor")
        TAYN = st.text_input("TAYN")
        LatestMilestoneFormSem = st.text_input("LatestMilestoneFormSem")
        InternationalStudentYN = st.text_input("InternationalStudentYN")
        Language = st.text_input("Language")
        LanguageDateFulfilled = st.text_input("LanguageDateFulfilled")
        LanguageReqWaivedBy = st.text_input("LanguageReqWaivedBy")
        LanguageReqWaivedDate = st.text_input("LanguageReqWaivedDate")
        ExamCommitteeFormDate = st.text_input("ExamCommitteeFormDate")
        ExamCommChair = st.text_input("ExamCommChair")
        ExamCommCoChair = st.text_input("ExamCommCoChair")
        ExamComm2nd = st.text_input("ExamComm2nd")
        ExamComm3rd = st.text_input("ExamComm3rd")
        FirstSemRegFEP = st.text_input("FirstSemRegFEP")
        ExamsCompleteDate = st.text_input("ExamsCompleteDate")
        ExamResult = st.text_input("ExamResult")
        RegDissPropSem = st.text_input("RegDissPropSem")
        ProposalApprovedDate = st.text_input("ProposalApprovedDate")
        DissertationTitle = st.text_input("DissertationTitle")
        CommitteeFormOnFileYN = st.text_input("CommitteeFormOnFileYN")
        DissCommChair = st.text_input("DissCommChair")
        DissCommCoChair = st.text_input("DissCommCoChair")
        DissComm2nd = st.text_input("DissComm2nd")
        DissComm3rd = st.text_input("DissComm3rd")
        DissComm4th = st.text_input("DissComm4th")
        AdditionalDissComm = st.text_input("AdditionalDissComm")
        GraduatedSemester = st.text_input("GraduatedSemester")
        Inactive = st.text_input("Inactive")
        Notes = st.text_input("Notes")
        MAProfessionalResearch = st.text_input("MAProfessionalResearch")
        LanguageSeePhD = st.text_input("LanguageSeePhD")
        PortfolioProposalApprovedDate = st.text_input("PortfolioProposalApprovedDate")
        CommitteeChair = st.text_input("CommitteeChair")
        CoChair = st.text_input("CoChair")
        Comm2 = st.text_input("Comm2")
        Comm3 = st.text_input("Comm3")
        DefenseDate = st.text_input("DefenseDate")
        Result = st.text_input("Result")
        GraduatedSem = st.text_input("GraduatedSem")
        InactiveCheck = st.text_input("InactiveCheck")
        PersonalEmail = st.text_input("PersonalEmail")
        Address = st.text_input("Address")
        Country = st.text_input("Country")
        Employment = st.text_input("Employment")
        SocialMedia = st.text_input("SocialMedia")
        AlumniNotes = st.text_input("AlumniNotes")
        if st.button("Filter"):
            message = st.warning("Here is the Filter result")
            studenter = search_student(lname, fname, studentid, Course, Program, ArtSchool, SubPlanText, FirstSemester, Catalog,HGHRcertCatalog, TranslCertCatalog, \
                            CRWcertCatalog, FacultyAdvisor, TAYN, LatestMilestoneFormSem, InternationalStudentYN \
                            , Language, LanguageDateFulfilled, LanguageReqWaivedBy, LanguageReqWaivedDate,ExamCommitteeFormDate, \
                            ExamCommChair, ExamCommCoChair, ExamComm2nd, ExamComm3rd, FirstSemRegFEP, ExamsCompleteDate, \
                            ExamResult, RegDissPropSem, ProposalApprovedDate, DissertationTitle, CommitteeFormOnFileYN, \
                            DissCommChair, DissCommCoChair, DissComm2nd, DissComm3rd, DissComm4th, AdditionalDissComm,GraduatedSemester, \
                            Inactive, Notes, MAProfessionalResearch, LanguageSeePhD, PortfolioProposalApprovedDate,CommitteeChair, \
                            CoChair, Comm2, Comm3, DefenseDate, Result, GraduatedSem, InactiveCheck, PersonalEmail, Address,Country, \
                            Employment, SocialMedia, AlumniNotes)
            st.table(studenter)
            time.sleep(2)
            message.empty()
    if selected == "View Database":
        student = view_students()
        st.table(student)




if __name__ == '__main__':
    main()