st.subheader("CGPA distribution")
fig2, ax2 = plt.subplots()
ax2.hist(view["CGPA"], bins=15)
ax2.set_xlabel("CGPA")
ax2.set_ylabel("Number of students")
st.pyplot(fig2)
# Key numbers
c1, c2, c3, c4 = st.columns(4)
c1.metric("Students", len(view))

if len(view) > 0:
    c2.metric("Average CGPA", f"{view['CGPA'].mean():.2f}")
    c3.metric("Average chance", f"{view['Chance of Admit'].mean():.0%}")
    c4.metric("Average GRE", f"{view['GRE Score'].mean():.1f}")
else:
    st.warning("No students match these filters. Lower the minimum CGPA.")
  min_cgpa = st.sidebar.slider("Minimum CGPA", 6.5, 10.0, 9.0, 0.1)
